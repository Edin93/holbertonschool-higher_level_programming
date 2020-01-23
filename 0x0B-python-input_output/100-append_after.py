#!/usr/bin/python3
""" This module contains only a single function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append new string after the line containing the search string.
    """
    with open(filename, 'r+') as f:
        data = f.readlines()

    new = []
    for i in range(len(data)):
        new.append(data[i])
        if search_string in data[i]:
            new.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new)
