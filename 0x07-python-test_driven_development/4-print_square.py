#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our print_square() function module, Ex:
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Print a square with the given size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/4-print_square.txt')
