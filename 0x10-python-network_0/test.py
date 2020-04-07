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
            if (l[p - 1] == l[p] or l[p + 1] == l[p]):
                p += 1
            elif  p + 1 < len(l) and l[p] > l[p - 1] and l[p] > l[p + 1]:
                return l[p]
            elif l[p - 1] > l[p]:
                if p + 1 < len(l) and l[p] > l[p + 1]:
                    if p + 2 < len(l):
                        p += 2
                elif p + 1 < len(l):
                    p += 1
            elif p + 1 < len(l) and l[p + 1] > l[p]:
                p += 1
            elif l[p - 1] < l[p] and p + 1 < len(l) and l[p] < l[p + 1]:
                p += 1
            elif p + 1 < len(l) and l[p + 1] > l[p]:
                if p + 2 < len(l) and l[p + 2] < l[p + 1]:
                    return l[p + 1]
        print("PPPP ====== ", p)
        return l[p]
