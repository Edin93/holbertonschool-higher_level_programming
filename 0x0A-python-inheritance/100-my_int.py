#!/usr/bin/python3
""" Module contains a single class.
"""


class MyInt(int):
    """
    Class MyInt inherits from the int built-int class.
    """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
