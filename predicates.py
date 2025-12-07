# For all functions we are going to assume that we have identified the coefficient matrix and constant vector
# From augmented matrix

# Checks if coefficient matrix is a square matrix or not 
def is_square(coe_matrix: ndarray):
    rows,columns = coe_matrix.shape #Storing dimensions of matrix
    if rows == columns: 
        return True
    else: return False

# Checks if coefficient matrix is diagnoally dominant
def is_diag_dom(coe_matrix: ndarray):
    #Take the summation of a row not including the pivot
    def row_sum(vec: ndarray,pivot: int) -> float: 
        total=0
        for j in range(cmax): 
            if(j != pivot):
                total += abs(vec[j])
        return total
    #For all rows, compare the row summation to the pivot value
    # If greater than, the matrix is not diagonally dominant
    for i in range(rmax):
        if abs(coe_matrix[i,i]) < row_sum(aug_matrix[i], i):
            return False 
    return True 

