#!/usr/bin/python3
""" This module contains a single class MyList that inherits from list.
"""


class MyList(list):
    """
    Class inherits from list and sort its content.
    """
    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        """
        print(sorted(self))