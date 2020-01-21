#!/usr/bin/python3
""" This module contains a single function.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
