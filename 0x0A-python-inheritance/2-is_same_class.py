#!/usr/bin/python3
""" This modules contains one function.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    otherwise False.
    """
    if str(a_class) == "<class 'object'>":
        return False
    else:
        return isinstance(obj, a_class)
