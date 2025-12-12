import numpy as np
from numpy import ndarray

def is_diag_dom(coe_matrix: ndarray) -> bool:
    """
    Checks if the coefficient matrix is diagonally dominant.
    Returns True if it is, False otherwise.
    """
    rmax, cmax = coe_matrix.shape
    if rmax != cmax:
        raise ValueError("Matrix must be square to check diagonal dominance")
    def row_sum(vec: ndarray, pivot: int) -> float:
        return sum(abs(vec[j]) for j in range(cmax) if j != pivot)
    for i in range(rmax):
        if abs(coe_matrix[i, i]) < row_sum(coe_matrix[i], i):
            return False
    return True
