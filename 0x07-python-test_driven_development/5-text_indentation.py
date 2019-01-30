#!/usr/bin/python3
""" Contains function which indents text """


def text_indentation(text):
    """ Indents text with 2 new lines after '.', '?', and ':' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        print(c, end="")
        if c in ['.', '?', ':']:
            print('\n')
