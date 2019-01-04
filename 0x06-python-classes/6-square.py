#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Contains square size"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        i = self.__position[1]
        while i:
            print()
            i -= 1
        i = self.__size
        while i:
            j = self.__position[0]
            while j:
                print(" ", end="")
                j -= 1
            j = self.__size
            while j:
                print("#", end="")
                j -= 1
            print()
            i -= 1

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
