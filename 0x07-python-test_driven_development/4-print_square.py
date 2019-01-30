#!/usr/bin/python3
""" Contains function which prints a square """


def print_square(size):
    """ Prints a square using '#' character """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
