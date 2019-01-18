#!/usr/bin/python3
""" Contains function which returns dict description with data scructure """


def class_to_json(obj):
    return obj.__dict__
