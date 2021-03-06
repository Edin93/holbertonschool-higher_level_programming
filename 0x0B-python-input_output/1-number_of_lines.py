#!/usr/bin/python3
""" This module contains a single function.
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of text file.
    """

    line_numbers = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line_numbers += 1

    return line_numbers
