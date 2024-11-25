"""
Two matrices must have an equal number of rows and columns to be subtracted.
In which case, the subtracted of two matrices A and B will be a matrix which
has the same number of rows and columns as A and B.

The result of the subtraction of A and B, denoted A - B is computed by subtracting corresponding elements of A and B.

Create a function that takes 2 x 2D lists lst1 and lst2 as an argument and returns a 2D list (matrix C). C = A-B.

Examples
subtract_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
"""

def subtract_matrix(matrix1, matrix2):
    # Check if matrices are same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error - matrices are not same dimensions"
    # Create return matrix, same dimensions as matrix1 (needs to be dynamic to matrix size)
    matrix3 = [[None] * len(matrix1) for i in range(len(matrix1[0]))]
    # Iterate through each cell of matrix
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            print(matrix1[i][j])
    # Perform subtraction operation
    # Populate return matrix


print(subtract_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
