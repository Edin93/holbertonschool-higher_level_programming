#!/usr/bin/python3
""" This module contains a single function.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure for JSON obj.
    """
    return obj.__dict__
