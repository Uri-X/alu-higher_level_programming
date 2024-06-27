#!/usr/bin/python3
"""
0-square_matrix_simple.py
Compute the square values of integers in a matrix and return a new matrix with squared values.
"""
# Function to compute square values of integers in a matrix
def square_matrix_simple(matrix):
    """
    Computes the square values of integers in the input matrix.
    Args:
        matrix (list of lists): 2D list of integers.
    Returns:
        list of lists: 2D list where each element is the square of the corresponding element in the input matrix.
    """
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for elem in row:
            squared_row.append(elem ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix
# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = square_matrix_simple(matrix)
    for row in result:
        print(row)
