#!/usr/bin/python3
""" Defines a class with no class or object attribute """

class LockedClass():
    """ prevents the user from dynamically creating new instance attributes

    >>> full_name = LockedClass()
    >>> full_name.first_name = "Wescott"
    >>> full_name.first_name
    "Wescott"

    >>> full_name.last_name = "Sharples"
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
