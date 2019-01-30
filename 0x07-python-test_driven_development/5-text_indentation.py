#!/usr/bin/python3
""" Contains function which indents text """


def text_indentation(text):
    """ Indents text with 2 new lines after '.', '?', and ':' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print('\n')
            c += 1
            while text[c] in " \n\t\v":
                c += 1
        else:
            c += 1
