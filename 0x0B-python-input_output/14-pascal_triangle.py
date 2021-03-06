#!/usr/bin/python3
""" This module contains a single function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of int representing pascal's triangle of n.
    """
    if n <= 0:
        return []
    else:
        rl = []
        for row in range(1, n + 1):
            cl = []
            for col in range(1, row + 1):
                if col == 1:
                    cl.append(1)
                elif col > len(rl[row - 2]):
                    cl.append(1)
                else:
                    cl.append(rl[row - 2][col - 2] + rl[row - 2][col - 1])
            rl.append(cl)
    return rl
