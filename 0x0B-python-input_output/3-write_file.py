#!/usr/bin/python3
""" This module contains a single function.
"""


def write_file(filename="", text=""):
    """
    Writes text to file(filename) and returns number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        chars_num = f.write(text)

    return chars_num
