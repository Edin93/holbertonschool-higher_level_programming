#!/usr/bin/python3
""" This module contains a single function.
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads nb lines from file and prints it to stdout.
    """

    total_lines = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1

    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines >= total_lines:
            print(f.read(), end='')
        else:
            for i in range(nb_lines):
                print(f.readline(), end='')
