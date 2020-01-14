#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our add_integers() function module, Ex:
>>> andd_integers(15, 235)
250
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b.
    """
    ip = float('inf')
    im = float('inf')
    if a != a or a == ip or a == im or isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if b != b or b == ip or b == im or isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/0-add_integer.txt')
