#!/usr/bin/python3
"""Find the peak of list of unsorted ints"""

def binary_search(loi, low, high):
    if low == high:
        return loi[low]
    mid = (low + high) // 2
    if loi[mid] > loi[mid + 1]:
        return binary_search(loi, low, mid)
    return binary_search(loi, mid + 1, high)

def find_peak(list_of_integers):
    """Calls binary search function"""
    if list_of_integers:
        return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
