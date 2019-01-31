#!/usr/bin/python3
""" Contains function that returns list of object attributes """


def lookup(obj):
    """ Returns list of object attributes and methods """
    return obj.__dict__
