#!/usr/bin/python3
""" Contains function which inserts a line of text to a file
    after each line which contains a specific string """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+", encoding="utf-8") as f:
        new = ""
        for line in f:
            if search_string in line:
                line += new_string
            new += line

        f.seek(0)
        f.write(new)
