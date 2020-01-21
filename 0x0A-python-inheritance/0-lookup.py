#!/usr/bin/python3
"""This is a simple module that has only a single function lookup.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of obj.
    """
    return dir(obj)
