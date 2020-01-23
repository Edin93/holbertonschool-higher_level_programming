#!/usr/bin/python3
""" This module contains a single class MyList that inherits from list.
"""


class MyList(list):
    """
    Class inherits from list and sort its content.
    """
    def __getitem__(self, key):
        """
        Get item.
        """
        return list.__getitem__(self, key-1)

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
