def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in row] for row in matrix]

    # Iterate over the rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square value of each integer
            result[i][j] = matrix[i][j] ** 2

    # Return the new matrix
    return result