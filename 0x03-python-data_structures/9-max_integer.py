#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return

    biggest = my_list[0]
    for i in my_list:
        if biggest < i:
            biggest = i
    return biggest
