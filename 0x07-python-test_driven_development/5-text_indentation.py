#!/usr/bin/python3
"""Contains a function that indents after ., ?, and :"""


def text_indentation(text):
    """Indents text after ., ?, and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for c in text:
        if flag == 1:
            continue
        else if c == ' ':
            continue
        else:
            flag = 0
        print(c, end="")
        if i in ['.', ':', '?']:
            print("\n")
            flag = 1
