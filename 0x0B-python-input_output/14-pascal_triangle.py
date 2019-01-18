#!/usr/bin/python3
""" Contains function that returns a list of integer lists
    representing Pascal's triangle of n """


def pascal_triangle(n):
    if n <= 0:
        return []

    tri = []
    for row in range(n):
        tri.append([1])
        for i in range(1, row):
            tri[row].append(tri[row - 1][i - 1] + tri[row - 1][i])
        if row is not 0:
            tri[row].append(1)
    return tri
