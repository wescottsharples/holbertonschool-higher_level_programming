#!/usr/bin/python3
"""Contains function that returns the sum of two ints"""


def add_integer(a, b=98):
    """Returns sum of two ints, second parameter defaults to 98"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
