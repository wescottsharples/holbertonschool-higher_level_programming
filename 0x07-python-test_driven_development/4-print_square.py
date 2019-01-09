#!/usr/bin/python3
"""Contains function that prints a square"""


def print_square(size):
    """Prints a square made of # symbol"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    row = '#' * size
    for i in range(size):
        print(row)
