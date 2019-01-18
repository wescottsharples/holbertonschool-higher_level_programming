#!/usr/bin/python3
""" Contains function which reads from a file """


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
