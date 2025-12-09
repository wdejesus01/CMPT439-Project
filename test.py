import tkinter as tk
from tkinter import messagebox
import numpy as np

# Define matrix size
n_rows = 3
n_cols = 4  # last column is augmented part (constants)

# Create main window
root = tk.Tk()
root.title("Augmented Matrix Solver")

# List to hold Entry widgets
entries = []

# Instructions
tk.Label(root, text=f"Enter augmented matrix ({n_rows}x{n_cols}):").grid(row=0, column=0, columnspan=n_cols)

# Create grid of Entry widgets
for r in range(n_rows):
    row_entries = []
    for c in range(n_cols):
        e = tk.Entry(root, width=5)
        e.grid(row=r+1, column=c, padx=2, pady=2)
        row_entries.append(e)
    entries.append(row_entries)

# Result label
result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=n_rows+2, column=0, columnspan=n_cols)

def solve_matrix():
    try:
        # Build numpy array from entries
        matrix = np.zeros((n_rows, n_cols))
        for r in range(n_rows):
            for c in range(n_cols):
                val = entries[r][c].get()
                matrix[r, c] = float(val)
        
        # Separate A and b
        A = matrix[:, :-1]
        b = matrix[:, -1]
        
        # Solve
        x = np.linalg.solve(A, b)
        solution_str = ", ".join([f"x{i+1}={val:.3f}" for i,val in enumerate(x)])
        result_label.config(text=f"Solution: {solution_str}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or no solution: {e}")

# Solve button
solve_btn = tk.Button(root, text="Solve", command=solve_matrix)
solve_btn.grid(row=n_rows+1, column=0, columnspan=n_cols, pady=5)

root.mainloop()
