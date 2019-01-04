#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Contains square size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        i = self.__size
        while i:
            j = self.__size
            while j:
                print("#", end="")
                j -= 1
            print()
            i -= 1

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
