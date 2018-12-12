#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return
    for r in range(len(matrix)):
        for i in range(len(matrix[r])):
            if (i < len(matrix[r]) - 1):
                print("{:d}".format(matrix[r][i]), end=" ")
            else:
                print("{:d}".format(matrix[r][i]))
