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
        pi = 0
        peak = l[pi]
        while pi < len(l):
            if pi == 0 and pi + 1 < len(l) and (l[0] > l[1] or l[0] == l[1]):
                peak = l[0]
            if pi + 1 < len(l) and l[pi - 1] < l[pi] and l[pi] > l[pi + 1]:
                if l[pi] > peak:
                    peak = l[pi]
            pi += 1
    return peak
