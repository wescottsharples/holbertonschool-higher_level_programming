#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" ")
        print()
