import re
from methods import *
import tkinter as  tk
from tkinter import * 
from tkinter import ttk
from typing import Sequence, Callable
import numpy as np

# --- Options Class --- # 
class Options:
    """
    Options for a user to call an iterative method with.
    """
    def __init__(self,
                 iter_func: str = "Jacobi",
                 err_func: str="Mean Absolute Approximate Error",
                 dimension: int = 3,
                 threshold: float = 1.0e-3,
                 init_aprox: Sequence = None):

        # method used (jacobi, gauss_seidel, etc.)
        self._iter_func = tk.StringVar(value=iter_func)
        # error metric function
        self._err_func = tk.StringVar(value=err_func)
        # runtime options
        self._dimension = tk.IntVar(value=dimension)
        self._threshold = tk.DoubleVar(value=threshold)
        # if user doesn't supply initial approximation or is not the right size: supply default
        if init_aprox is None or len(init_aprox) != self._dimension:
            self._init_aprox = np.ones(dimension)
        else: 
            self._init_aprox = np.array(init_aprox)

     #  self._dimension.trace_add("write",
    

    # ------------ Getters ----------------
    def getIterFunc(self):
        return self._iter_func
    def getErrFunc(self):
        return self._err_func
    def getDimension(self):
        return self._dimension
    def getThreshold(self):
        return self._threshold
    def getInitAprox(self):
        return self._init_aprox
    # ------------ Setters ----------------
    def setDimension(self, dimension: int):
        self._dimension = dimension
        # update init vector size accordingly
        self._init_aprox = np.ones(dimension)
    def setInitAprox(self, init_aprox: Sequence):
        if len(init_aprox) == self._dimension.get():
            self._init_aprox = np.array(init_aprox)
        else:  
            print(f"Initial approximation size {len(init_aprox)} does not match "
                  f"dimension {self._dimension}. Defaulting to ones().")
            self._init_aprox = np.ones(self._dimension.get())

# One row for for each options attribute
# 1st column of row is a label displaying attribute name
# 2nd column of row is a label displaing current attribute value
# 3rd column is a interactable widget that will take input and set a new value 

# ---Options  window & Frame---  #
root= Tk()
root.title("Options")
root.columnconfigure(0, weight=1)
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

test = Options()
# --- Grid Headers --- #
opt_header = ttk.Label(mainframe, text="Options")
cur_val = ttk.Label(mainframe, text= "Current Value") 
set_val = ttk.Label(mainframe, text= "New Value")
headers =  [opt_header, cur_val, set_val]
for i, header in enumerate(headers):
   header.grid(row = 0, column=i,sticky='NE')
   mainframe.columnconfigure(i, weight=1) # Resizable columns

# --- Options Column  --- #
#Tuple(immutable) of option names
options = ("Iterative Method",
                "Error Equation",
                "Dimension",
                "Initial Approximates",
                "Threshold")
for i, option in enumerate(options):
    ttk.Label(mainframe, text=options[i]).grid(row=i+1, column=0)

# --- Current Values Column --- #
# Bind every displayed current-value label to the corresponding StringVar / IntVar / DoubleVar
test = Options()
ttk.Label(mainframe, textvariable=test.getDimension()).grid(column=1, row=2)
# Iterative method (StringVar)
ttk.Label(mainframe, textvariable=test.getIterFunc()).grid(row=1, column=1)
# Error function (StringVar)
ttk.Label(mainframe, textvariable=test.getErrFunc()).grid(row=2, column=1)
# Dimension (IntVar)
ttk.Label(mainframe, textvariable=test.getDimension()).grid(row=3, column=1)
# Initial Approximates (array → convert to string)
init_label_var = tk.StringVar()
init_label_var.set(str(test.getInitAprox()))
ttk.Label(mainframe, textvariable=init_label_var).grid(row=4, column=1)
# Threshold (DoubleVar)
ttk.Label(mainframe, textvariable=test.getThreshold()).grid(row=5, column=1)

# --- New Value Column--- #

def floatP(entry):
    """Validates floating point strings"""
    return re.fullmatch("^[0-9]+\\.?[0-9]*$", entry) is not None 
floatP_wrapper = (mainframe.register(floatP), '%P')

def intP(entry):
    """Validates Integer Strings"""
    return re.fullmatch("^[0-9]*$", entry) is not None and len(entry) < 6 #Arbiturary limit 
intP_wrapper = (mainframe.register(intP), '%P')

threshold=ttk.Entry(mainframe, textvariable=test.getThreshold(), validate='key', validatecommand=floatP_wrapper) 
threshold.grid(column=2, row=5)
dimension=ttk.Entry(mainframe,textvariable=test.getDimension(), validate='key', validatecommand=intP_wrapper)
dimension.grid(column=2, row=3)

# --- Method Selection Widgets --- #
method = StringVar()
jacobi = ttk.Radiobutton(mainframe, text="Jacobi",variable=test.getIterFunc(), value="Jacobi")
gauss_seidel = ttk.Radiobutton(mainframe, text="Gauss Seidel",variable=test.getIterFunc(), value="Gauss Seidel")
jacobi.grid(column=2,row=1)
gauss_seidel.grid(column=3, row=1)

# --- Error Selection Widgets --- #
error = ttk.Combobox(mainframe, textvariable=test.getErrFunc(), state=["readonly"],
                     width=25)
error['values'] = ("Mean Absolute Approximate Error",
                "Approximate Root Mean Square Error",
                "True Mean Asbolute Error",
                "True Root Mean Square Error")
error.grid(column=2, row =2)

# === Initial Approximates === #
# Frame holding vector entries; 
# Used to delete and replace vector when size changes #
vector_frame= ttk.Frame(mainframe, relief='raised')
vector_frame.grid(column=3,row=4)

# Retrieve column and row for widget
def locate(widget):
    widgInfo = widget.grid_info() 
    return [widgInfo[k] for k in ('row','column')]

# Create a row of entries of size N inside of a frame/window
def createRow(parent, size: int, r_offset: int, c_offset: int):
    entry_row = []
    for i in range(size):
        ttk.Entry(parent, width=5).grid(row=r_offset, column=c_offset + i)

# Create a vector out of initial approximates
# Parent widget(frame) must only contain widgets
def getEntryRow(size: int, parent) -> Sequence[float]:
    row = []
    for entry in parent.winfo_children():
        print(entry.get())
        row.append(entry.get())
    return row

createRow(vector_frame,3,*locate(vector_frame))




def recreateRow(parent, size: int):
    for entry in parent.winfo_children():
        entry.destroy()
    r_offset, c_offset= locate(parent)
    createRow(parent,size,r_offset, c_offset)
    test.setInitAprox(np.ones(size))
    init_label_var.set(str(test.getInitAprox()))

def on_dimension_change(*args):
    size = test.getDimension().get()
    recreateRow(vector_frame, size)

test.getDimension().trace_add("write", on_dimension_change)
recreateRow(vector_frame, test.getDimension().get())

root.mainloop() # Start event loop
import re
import tkinter as tk
from tkinter import ttk
import numpy as np

# --- Options Class --- #
class Options:
    def __init__(self,
                 iter_func: str = "Jacobi",
                 err_func: str="Mean Absolute Approximate Error",
                 dimension: int = 3,
                 threshold: float = 1.0e-3,
                 init_aprox: list = None):

        self._iter_func = tk.StringVar(value=iter_func)
        self._err_func = tk.StringVar(value=err_func)
        self._dimension = tk.IntVar(value=dimension)
        self._threshold = tk.DoubleVar(value=threshold)
        if init_aprox is None or len(init_aprox) != self._dimension.get():
            self._init_aprox = np.ones(dimension)
        else:
            self._init_aprox = np.array(init_aprox)

    def getIterFunc(self): return self._iter_func
    def getErrFunc(self): return self._err_func
    def getDimension(self): return self._dimension
    def getThreshold(self): return self._threshold
    def getInitAprox(self): return self._init_aprox
    def setDimension(self, dimension: int):
        self._dimension.set(dimension)
        self._init_aprox = np.ones(dimension)
    def setInitAprox(self, init_aprox: list):
        if len(init_aprox) == self._dimension.get():
            self._init_aprox = np.array(init_aprox)
        else:
            self._init_aprox = np.ones(self._dimension.get())

# --- Helper Functions --- #
def locate(widget):
    info = widget.grid_info()
    return info['row'], info['column']

def floatP(entry):
    """Validate floating point numbers."""
    return re.fullmatch(r"^[+-]?\d*\.?\d*$", entry) is not None

def createRow(parent, size, r_offset, c_offset, options, init_label_var):
    """Create a row of Entry widgets bound to an Options instance, only allowing floats."""
    float_wrapper = (parent.register(floatP), '%P')  # Validate floating-point input
    
    def make_callback(var, index):
        def callback(*args):
            try:
                options._init_aprox[index] = float(var.get())
            except ValueError:
                pass
            init_label_var.set(str(options.getInitAprox()))
        return callback

    for idx in range(size):
        var = tk.StringVar(value=str(options.getInitAprox()[idx]))
        var.trace_add("write", make_callback(var, idx))
        ttk.Entry(parent, width=6, textvariable=var, justify='center', font=("Arial", 11),
                  validate='key', validatecommand=float_wrapper).grid(
            row=r_offset, column=c_offset + idx, padx=4, pady=4
        )

def recreateRow(parent, size, options, init_label_var):
    r_offset, c_offset = locate(parent)
    for entry in parent.winfo_children():
        entry.destroy()
    options.setInitAprox(np.ones(size))
    createRow(parent, size, r_offset, c_offset, options, init_label_var)
    init_label_var.set(str(options.getInitAprox()))

def bind_dimension_change(options, vector_frame, init_label_var):
    def on_dimension_change(*args):
        recreateRow(vector_frame, options.getDimension().get(), options, init_label_var)
    options.getDimension().trace_add("write", on_dimension_change)

# --- GUI Setup --- #
root = tk.Tk()
root.title("Options Panel")
root.geometry("700x400")
root.configure(bg="#f0f0f0")

options1 = Options()

mainframe = ttk.Frame(root, padding=15, relief='raised')
mainframe.grid(column=0, row=0, sticky='NSEW')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --- Headers --- #
headers = ["Options", "Current Value", "New Value"]
for i, text in enumerate(headers):
    lbl = ttk.Label(mainframe, text=text, font=("Arial", 12, "bold"),
                    background="#d9e2f3", anchor="center", padding=5)
    lbl.grid(row=0, column=i, sticky="EW", padx=2, pady=2)
    mainframe.columnconfigure(i, weight=1)

# --- Labels Column --- #
options_labels = ["Iterative Method", "Error Equation", "Dimension", "Initial Approximates", "Threshold"]
for i, text in enumerate(options_labels):
    lbl = ttk.Label(mainframe, text=text, font=("Arial", 11), padding=5, anchor="w")
    lbl.grid(row=i+1, column=0, sticky='W')

# --- Current Value Column --- #
ttk.Label(mainframe, textvariable=options1.getIterFunc(), font=("Arial", 11)).grid(row=1, column=1)
ttk.Label(mainframe, textvariable=options1.getErrFunc(), font=("Arial", 11)).grid(row=2, column=1)
ttk.Label(mainframe, textvariable=options1.getDimension(), font=("Arial", 11)).grid(row=3, column=1)

init_label_var = tk.StringVar()
init_label_var.set(str(options1.getInitAprox()))
ttk.Label(mainframe, textvariable=init_label_var, font=("Arial", 11)).grid(row=4, column=1)
ttk.Label(mainframe, textvariable=options1.getThreshold(), font=("Arial", 11)).grid(row=5, column=1)

# --- New Value Column --- #
floatP_wrapper = (mainframe.register(floatP), '%P')
intP_wrapper = (mainframe.register(lambda e: re.fullmatch(r"^[0-9]*$", e) is not None and len(e)<6), '%P')

ttk.Entry(mainframe, textvariable=options1.getThreshold(),
          validate='key', validatecommand=floatP_wrapper, font=("Arial", 11)).grid(column=2, row=5, padx=4, pady=4)
ttk.Entry(mainframe, textvariable=options1.getDimension(),
          validate='key', validatecommand=intP_wrapper, font=("Arial", 11)).grid(column=2, row=3, padx=4, pady=4)

# --- Iterative Method Widgets --- #
ttk.Radiobutton(mainframe, text="Jacobi", variable=options1.getIterFunc(), value="Jacobi").grid(column=2, row=1, padx=4, pady=4)
ttk.Radiobutton(mainframe, text="Gauss Seidel", variable=options1.getIterFunc(), value="Gauss Seidel").grid(column=3, row=1, padx=4, pady=4)

# --- Error Function Widgets --- #
error_cb = ttk.Combobox(mainframe, textvariable=options1.getErrFunc(),
                        state="readonly", width=35, font=("Arial", 11))
error_cb['values'] = ("Mean Absolute Approximate Error",
                      "Approximate Root Mean Square Error",
                      "True Mean Absolute Error",
                      "True Root Mean Square Error")
error_cb.grid(column=2, row=2, padx=4, pady=4, columnspan=2, sticky='EW')

# --- Initial Approximates --- #
vector_frame = ttk.Frame(mainframe, relief='raised', padding=5)
vector_frame.grid(column=2, row=4, columnspan=2, sticky='W', padx=4, pady=4)

createRow(vector_frame, options1.getDimension().get(), 0, 0, options1, init_label_var)
bind_dimension_change(options1, vector_frame, init_label_var)

root.mainloop()
