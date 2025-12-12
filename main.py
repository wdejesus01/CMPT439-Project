import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
#from options import *


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