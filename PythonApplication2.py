import csv

def read_csv_to_matrix(filename):
    # open the file in read mode
    with open(filename, 'r') as file:
        # create a csv reader object
        csv_reader = csv.reader(file)
        
        # convert all rows to a list (matrix)
        matrix = list(csv_reader)
    
    return matrix

# replace 'your_file.csv' with your actual csv filename
filename = 'your_file.csv'

# call the function with the filename
matrix = read_csv_to_matrix(filename)

# print row by row
print("printing row by row:")
for row in matrix:
    print(row)