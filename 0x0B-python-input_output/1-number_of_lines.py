#!/usr/bin/python3
""" Contains function which counts lines in file """


def number_of_lines(filename=""):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
        return count
