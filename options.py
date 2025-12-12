import tkinter as tk
from tkinter import ttk
import numpy as np
import re

# --- Options Class --- #
class Options:
    def __init__(self, iter_func="Jacobi", err_func="Mean Absolute Approximate Error",
                 dimension=3, threshold=1.0e-3, init_aprox=None):
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
    def setDimension(self, dimension): 
        self._dimension.set(dimension)
        self._init_aprox = np.ones(dimension)
    def setInitAprox(self, init_aprox):
        if len(init_aprox) == self._dimension.get():
            self._init_aprox = np.array(init_aprox)
        else:
            self._init_aprox = np.ones(self._dimension.get())

# --- Options Frame --- #
class OptionsFrame(ttk.Frame):
    def __init__(self, parent, options_instance, show_main_callback):
        super().__init__(parent, padding=10, relief="raised")
        self.options = options_instance
        self.show_main_callback = show_main_callback

        # Headers
        headers = ["Options", "Current Value", "New Value"]
        for i, text in enumerate(headers):
            lbl = ttk.Label(self, text=text, font=("Arial", 12, "bold"),
                            anchor="center", padding=5)
            lbl.grid(row=0, column=i, sticky="EW", padx=2, pady=2)
            self.columnconfigure(i, weight=1)

        labels = ["Iterative Method", "Error Equation", "Dimension", "Initial Approximates", "Threshold"]
        for i, text in enumerate(labels):
            ttk.Label(self, text=text, font=("Arial", 11), anchor="w").grid(row=i+1, column=0, sticky="w")

        # Current Values
        ttk.Label(self, textvariable=self.options.getIterFunc()).grid(row=1, column=1)
        ttk.Label(self, textvariable=self.options.getErrFunc()).grid(row=2, column=1)
        ttk.Label(self, textvariable=self.options.getDimension()).grid(row=3, column=1)

        self.init_label_var = tk.StringVar(value=str(self.options.getInitAprox()))
        ttk.Label(self, textvariable=self.init_label_var).grid(row=4, column=1)
        ttk.Label(self, textvariable=self.options.getThreshold()).grid(row=5, column=1)

        # New value widgets
        floatP_wrapper = (self.register(lambda e: re.fullmatch(r"^[+-]?\d*\.?\d*$", e) is not None), '%P')
        intP_wrapper = (self.register(lambda e: re.fullmatch(r"^[0-9]*$", e) is not None and len(e)<6), '%P')

        ttk.Entry(self, textvariable=self.options.getThreshold(), validate='key', validatecommand=floatP_wrapper).grid(column=2, row=5, padx=4, pady=4)
        ttk.Entry(self, textvariable=self.options.getDimension(), validate='key', validatecommand=intP_wrapper).grid(column=2, row=3, padx=4, pady=4)

        # Iterative methods
        ttk.Radiobutton(self, text="Jacobi", variable=self.options.getIterFunc(), value="Jacobi").grid(column=2, row=1)
        ttk.Radiobutton(self, text="Gauss Seidel", variable=self.options.getIterFunc(), value="Gauss Seidel").grid(column=3, row=1)

        # Error combobox
        error_cb = ttk.Combobox(self, textvariable=self.options.getErrFunc(), state="readonly")
        error_cb['values'] = ("Mean Absolute Approximate Error",
                              "Approximate Root Mean Square Error",
                              "True Mean Absolute Error",
                              "True Root Mean Square Error")
        error_cb.grid(column=2, row=2, columnspan=2, sticky='EW')

        # Initial Approx vector
        self.vector_frame = ttk.Frame(self, relief='solid', padding=5)
        self.vector_frame.grid(column=2, row=4, columnspan=2, sticky='W')
        self.create_init_row()
        self.options.getDimension().trace_add("write", lambda *args: self.create_init_row())

        # Back button
        ttk.Button(self, text="Back", command=self.show_main_callback).grid(row=6, column=0, columnspan=3, pady=10)

    def create_init_row(self):
        size = self.options.getDimension().get()
        float_wrapper = (self.register(lambda e: re.fullmatch(r"^[+-]?\d*\.?\d*$", e) is not None), '%P')
        for widget in self.vector_frame.winfo_children():
            widget.destroy()
        self.options.setInitAprox(np.ones(size))
        for idx in range(size):
            var = tk.StringVar(value=str(self.options.getInitAprox()[idx]))
            var.trace_add("write", self.make_callback(var, idx))
            ttk.Entry(self.vector_frame, width=6, textvariable=var, justify='center',
                      validate='key', validatecommand=float_wrapper).grid(row=0, column=idx, padx=4, pady=4)
        self.init_label_var.set(str(self.options.getInitAprox()))

    def make_callback(self, var, index):
        def callback(*args):
            try:
                self.options._init_aprox[index] = float(var.get())
            except ValueError:
                pass
            self.init_label_var.set(str(self.options.getInitAprox()))
        return callback
