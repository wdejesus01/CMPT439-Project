import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
from options import *
from methods import jacobi, gauss_seidel

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
        ttk.Label(self, text="Main Page", font=("Arial", 16)).pack(pady=20)
        ttk.Button(self, text="Go to Options", command=show_options_callback).pack()

# --- Main App --- #
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App with Options")
        self.geometry("800x500")

        self.options = Options()

        # Frames
        self.main_page = MainPage(self, self.options, self.show_options)
        self.options_page = OptionsFrame(self, self.options, self.show_main)

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

