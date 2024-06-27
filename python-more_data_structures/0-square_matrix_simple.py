# Function to compute square values of integers in a matrix
def square_matrix_simple(matrix):
    # Create a new matrix to store squared values
    squared_matrix = []
    # Iterate through each row in the matrix
    for row in matrix:
        # Create a new row for the squared values
        squared_row = []
        # Iterate through each element in the row
        for elem in row:
            # Square the element and append to squared_row
            squared_row.append(elem ** 2)
        # Append the squared_row to the squared_matrix
        squared_matrix.append(squared_row)
    # Return the squared_matrix
    return squared_matrix
