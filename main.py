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

# Example usage:
selected_error_name = options1.getErrFunc().get()  # e.g., "Mean Absolute Approximate Error"
selected_error_code = error_map[selected_error_name]  # returns 0 for the above
root = tk.Tk()
root.title('Welcome to the linear algebraic equations solver')
label = tk.Label(root, text="Please click one of the following")
op1 = tk.Button(root, text="option1",command=root.destroy)
op1.pack()
op2 = tk.Button(root, text="option2",command=root.destroy)
op2.pack()

op3 = tk.Button(root, text="option3",command=root.destroy)
op3.pack()
op4 = tk.Button(root, text="option4",command=root.destroy)
op4.pack()
label.pack()
root.mainloop()

"""

"""
