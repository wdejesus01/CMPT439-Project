from tkinter import filedialog
import csv
import numpy as np
import predicates 

# === Read a CSV file and return appropriate Matrix === #
# Checks if matrix specified by CSV is square 

def csv2matrix(filename):
    # open the file 
    with open(filename, newline='') as file:
        # create a csv reader object
        csv_row  = csv.reader(file,quoting=csv.QUOTE_NONNUMERIC)
        # convert all csv_rows to a list 
        matrix = [] 
        for row in csv_row:
            if row: #Checks if row is not empty
                matrix.append(row)
        matrix = np.array(matrix) #Numpy already checks for non-homogenity
        if predicates.is_square(matrix[:,:-1]): 
            return matrix
        else: 
            raise Exception("Augmented matrix in CSV file is not square")
            
# === File Selection === #
#Opens OS's default dialogue window for file selection
#Returns a empty string if user cancels dialogue
file = filedialog.askopenfilename(filetypes=[("CSV Files", ".csv")]) #Filter for CSV files
matrix = csv2matrix(file)
