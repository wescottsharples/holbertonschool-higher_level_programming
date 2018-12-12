#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list is None or idx is None:
        return None
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
