import csv
import numpy as np
from tkinter import filedialog
from options import Options

def csv2matrix(options: Options):
    """
    Opens a CSV file, reads an augmented matrix, validates it,
    and returns the matrix if it matches the expected size.
    The last column is assumed to be the RHS b.
    """
    # Open file dialog
    file = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV Files", "*.csv")]
    )
    if not file:
        return None  # User canceled

    # Read CSV
    with open(file, newline='') as f:
        csv_reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        matrix = [row for row in csv_reader if row]  # skip empty rows
        matrix = np.array(matrix, dtype=float)

    rows, columns = matrix.shape
    if columns != rows + 1:
        raise ValueError("CSV must contain a square matrix with an extra column for RHS b")
    if rows != options.getDimension().get():
        raise ValueError(f"Matrix size {rows} does not match current dimension {options.getDimension().get()}")

    return matrix
