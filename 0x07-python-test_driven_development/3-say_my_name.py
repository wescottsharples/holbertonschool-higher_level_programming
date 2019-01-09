#!/usr/bin/python3
"""Contains function that prints two strings"""


def say_my_name(first_name, last_name=""):
    """Prints first and last name as strings"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
