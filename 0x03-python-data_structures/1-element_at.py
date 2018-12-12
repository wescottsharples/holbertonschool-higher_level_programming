#!/usr/bin/python3
def element_at(my_list, idx):
    if (my_list is None) or (idx is None):
        return
    if (idx < 0):
        return
    elif (idx >= len(my_list)):
        return
    else:
        return my_list[idx]
