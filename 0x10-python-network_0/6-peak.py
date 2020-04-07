#!/usr/bin/python3
"""
Contains a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    l = list_of_integers
    if len(l) < 3:
        return None
    else:
        p = 1
        while p < len(l):
            if p + 1 < len(l) and l[p - 1] < l[p] and l[p] > l[p + 1]:
                return l[p]
            elif p + 1 < len(l):
                p += 1
            else:
                return l[p]
