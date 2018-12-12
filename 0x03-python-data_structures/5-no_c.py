#!/usr/bin/python3
def no_c(my_string):
    string_cpy = ""
    if (my_string is None):
        return
    for c in my_string:
        if (c != 'c' and c != 'C'):
            string_cpy += (c)
    return string_cpy
