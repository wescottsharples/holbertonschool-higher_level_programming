#!/usr/bin/python3
""" Module contains class Rectangle """


class Rectangle:
    """ Defines Rectangle class """

    def __init__(self, width=0, height=0):
        """ Inits class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves width attribute """
        return self.__width

    @property
    def height(self):
        """ Retrieves height attribute """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets width attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
