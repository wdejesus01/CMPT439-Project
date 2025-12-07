from tkinter import *
from tkinter import ttk
from typing import Sequence, Callable
import numpy as np

class Options:
    """
    Options for a user to call an iterative method with.
    """

    def __init__(self,
                 iter_func: Callable,
                 err_func: Callable,
                 dimension: int = 3,
                 threshold: float = 1.0e-3,
                 init_aprox: Sequence = None):

        # method used (jacobi, gauss_seidel, etc.)
        self._iter_func = iter_func
        # error metric function
        self._err_func = err_func
        # runtime options
        self._dimension = dimension
        self._threshold = threshold
        # if user doesn't supply initial approximation or is not the right size: supply default
        if init_aprox is None or len(init_aprox) != self._dimension:
            self._init_aprox = np.ones(dimension)
        else: 
            self._init_aprox = np.array(init_aprox)
    

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
    def setIterFunc(self, func: Callable):
        self._iter_func = func

    def setErrFunc(self, func: Callable):
        self._err_func = func

    def setDimension(self, dimension: int):
        self._dimension = dimension
        # update init vector size accordingly
        self._init_aprox = np.ones(dimension)

    def setThreshold(self, threshold: float):
        self._threshold = threshold

    def setInitAprox(self, init_aprox: Sequence):
        self._init_aprox = np.array(init_aprox)
