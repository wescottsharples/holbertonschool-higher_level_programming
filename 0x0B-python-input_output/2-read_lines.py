#!/usr/bin/python3
""" Contains function that reads n lines of a text file """


def read_lines(filename="", nb_lines=0):
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            while nb_lines:
                print(f.readline(), end="")
                nb_lines -= 1
