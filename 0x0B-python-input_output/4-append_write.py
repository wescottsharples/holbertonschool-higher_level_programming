#!/usr/bin/python3
""" Contains function that appends a string to end of file """


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
