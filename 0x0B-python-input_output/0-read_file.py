#!/usr/bin/python3
""" This module contains a single function.
"""


def read_file(filename=""):
    """
    Reads from a file.
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        data = f.read()
        print(data, end="")
