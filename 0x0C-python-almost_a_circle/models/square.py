#!/usr/bin/python3
""" contains class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """makes a class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        if args:
            keys = ["id", "size", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        sdict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return sdict