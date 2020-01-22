#!/usr/bin/python3
""" This module contains a single function.
"""


def append_write(filename="", text=""):
    """
    Appends text to file and returns number of characters added.
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        chars_number = f.write(text)

    return chars_number
