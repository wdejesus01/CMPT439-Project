import tkinter as tk
from tkinter import ttk, messagebox
import re
import numpy as np
from options import Options, OptionsFrame
from methods import jacobi, gauss_seidel
from file import csv2matrix  # CSV loader
from predicates import is_diag_dom  # Diagonal dominance check

# Map the method names to the actual callable functions
method_map = {
    "Jacobi": jacobi,
    "Gauss Seidel": gauss_seidel
}

# Map error strings to integers
error_map = {
    "Mean Absolute Approximate Error": 0,
    "Approximate Root Mean Square Error": 1,
    "True Mean Absolute Error": 2,
    "True Root Mean Square Error": 3
}

# --- Main Page --- #
class MainPage(ttk.Frame):
    def __init__(self, parent, options_instance, show_options_callback):
        super().__init__(parent, padding=20)
        self.options = options_instance
        self.show_options_callback = show_options_callback

        # Header and navigation
        ttk.Label(self, text="Main Page", font=("Arial", 16)).pack(pady=10)
        ttk.Button(self, text="Go to Options", command=self.show_options_callback).pack(pady=5)

        # Frame to hold the Ax=b system
        self.matrix_frame = ttk.Frame(self)
        self.matrix_frame.pack(pady=20)

        # Variables and labels
        self.matrix_vars = {}  # For A
        self.b_vars = {}       # For b
        self.x_labels = {}     # For x (unknowns)

        # Create the system initially
        self.create_matrix_system()

        # Update system if dimension changes
        self.options.getDimension().trace_add("write", lambda *args: self.create_matrix_system())

        # Solve button
        ttk.Button(self, text="Solve", command=self.solve_system).pack(pady=10)

        # Load CSV and solve button
        ttk.Button(self, text="Load CSV and Solve", command=self.load_csv_and_solve).pack(pady=5)

    def create_matrix_system(self):
        # Clear previous widgets
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        self.matrix_vars = {}
        self.b_vars = {}
        self.x_labels = {}
        size = self.options.getDimension().get()
        if size <= 0:
            return

        # Float validation from Options
        float_wrapper = (self.register(lambda e: re.fullmatch(r"^[+-]?\d*\.?\d*$", e) is not None), '%P')

        # --- Headers ---
        ttk.Label(self.matrix_frame, text="Matrix A", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=size, pady=2)
        ttk.Label(self.matrix_frame, text="Unknowns x", font=("Arial", 12, "bold")).grid(row=0, column=size+1, padx=10)
        ttk.Label(self.matrix_frame, text="RHS b", font=("Arial", 12, "bold")).grid(row=0, column=size+3, columnspan=1, padx=10)

        # --- Matrix A entries ---
        for i in range(size):
            for j in range(size):
                var = tk.StringVar(value="0")
                self.matrix_vars[(i, j)] = var
                ttk.Entry(self.matrix_frame, width=6, textvariable=var,
                          justify='center', validate='key', validatecommand=float_wrapper).grid(row=i+1, column=j, padx=2, pady=2)

        # --- Vector x (unknowns) centered ---
        for i in range(size):
            lbl = ttk.Label(self.matrix_frame, text="", width=6, relief="solid", anchor="center")
            lbl.grid(row=i+1, column=size+1, pady=2)
            self.x_labels[i] = lbl

        # --- Equal sign ---
        ttk.Label(self.matrix_frame, text="=", font=("Arial", 16)).grid(row=1, column=size+2, padx=10, rowspan=size, sticky="ns")

        # --- Vector b entries ---
        for i in range(size):
            var = tk.StringVar(value="0")
            self.b_vars[i] = var
            ttk.Entry(self.matrix_frame, width=6, textvariable=var,
                      justify='center', validate='key', validatecommand=float_wrapper).grid(row=i+1, column=size+3, padx=2, pady=2)

    def get_matrix(self):
        size = self.options.getDimension().get()
        A = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                try:
                    A[i, j] = float(self.matrix_vars[(i, j)].get())
                except ValueError:
                    A[i, j] = 0.0
        return A

    def get_rhs(self):
        size = self.options.getDimension().get()
        b = np.zeros(size)
        for i in range(size):
            try:
                b[i] = float(self.b_vars[i].get())
            except ValueError:
                b[i] = 0.0
        return b

    def solve_system(self):
        A = self.get_matrix()
        b = self.get_rhs()

        # --- Check diagonal dominance ---
        if not is_diag_dom(A):
            messagebox.showwarning("Warning", "Matrix is not diagonally dominant; solver may not converge.")

        method_name = self.options.getIterFunc().get()
        error_type = error_map[self.options.getErrFunc().get()]
        threshold = self.options.getThreshold().get()
        init_approx = self.options.getInitAprox()  # Use initial approximation from options

        solve_func = method_map.get(method_name, jacobi)

        try:
            # Pass initial approximation to solver
            x_solution = solve_func(
                np.column_stack((A, b)),  # augmented matrix
                threshold=threshold,
                stop=error_type,
                init_approx=init_approx
            )

            # Update x labels
            for i, val in enumerate(x_solution):
                self.x_labels[i].config(text=f"{val:.5f}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to solve system:\n{e}")

    def load_csv_and_solve(self):
        try:
            matrix = csv2matrix(self.options)
            if matrix is None:
                return  # user canceled

            A = matrix[:, :-1]
            b = matrix[:, -1]
            size = A.shape[0]

            # Update dimension in options and recreate the matrix system
            self.options.setDimension(size)
            self.create_matrix_system()

            # Fill matrix entries
            for i in range(size):
                for j in range(size):
                    self.matrix_vars[(i, j)].set(str(A[i, j]))
                self.b_vars[i].set(str(b[i]))

            # Solve immediately
            self.solve_system()

        except Exception as e:
            messagebox.showerror("CSV Load Error", str(e))

# --- Main App --- #
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linear System Solver")
        self.geometry("1000x600")

        self.options = Options()

        # Frames
        self.main_page = MainPage(self, self.options, self.show_options)
        self.options_page = OptionsFrame(self, self.options, self.show_main)

        # Show main page initially
        self.main_page.pack(fill="both", expand=True)

    def show_options(self):
        self.main_page.pack_forget()
        self.options_page.pack(fill="both", expand=True)

    def show_main(self):
        self.options_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)

# Run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
