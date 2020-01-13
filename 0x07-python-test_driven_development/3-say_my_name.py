#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our say_my_name() function module, Ex:
>>> say_my_name("Keanu", "Reeves")
My name is Keanu Reeves
"""


def say_my_name(first_name, last_name=""):
    """
    Prints fullname.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/3-say_my_name.txt')
