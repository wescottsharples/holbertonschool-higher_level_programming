#!/usr/bin/python3
""" Contains function which divides all elements of a matrix """


def matrix_divided(matrix, div):
    type_warning = "matrix must be a matrix (list of lists) of integers/floats"

    """ Divides all elements of a matrix """
    if not isinstance(matrix, list):
        raise TypeError(type_warning)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    if row_len == 0:
        raise TypeError(type_warning)
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_warning)
        if not len(row) == row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(type_warning)
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
