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
        if len(init_aprox) == self._dimension:
            self._init_aprox = np.array(init_aprox)
        else:  
            print(f"Initial approximation size {len(init_aprox)} does not match "
                  f"dimension {self._dimension}. Defaulting to ones().")
            self._init_aprox = np.ones(self._dimension)

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
# value labels with textvariable set to 
test = Options(jacobi)
ttk.Label(mainframe, textvariable=test.getDimension()).grid(column=1, row=2)

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
    r_offset, c_offset= locate(parent)
    for entry in parent.winfo_children():
        entry.destroy()
    createRow(parent,size,r_offset, c_offset)

recreateRow(vector_frame, 3)

root.mainloop() # Start event loop
