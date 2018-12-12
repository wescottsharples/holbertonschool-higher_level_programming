#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list is None) or (len(my_list) < 1):
        return

    true_list = []
    for i in my_list:
        if (i % 2 == 0):
            true_list.append(True)
        else:
            true_list.append(False)

    return true_list
