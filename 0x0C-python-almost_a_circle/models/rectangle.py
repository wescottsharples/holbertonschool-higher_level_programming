#!/usr/bin/python3
""" contains class Rectangle """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    def area(self):
        return self.width * self.height

    def update(self, *args, **kwargs):
        argc = len(args)
        if argc > 0:
            self.id = args[0]
        if argc > 1:
            self.width = args[1]
        if argc > 2:
            self.height = args[2]
        if argc > 3:
            self.x = args[3]
        if argc > 4:
            self.y = args[4]
        if argc == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def display(self):
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def to_dictionary(self):
        """dictionary"""
        rdict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
        return rdict

    def __str__(self):
        """
        This function returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    """ invalid """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
