#!/usr/bin/python3
""" This module contains a single class.
"""


class BaseGeometry:
    """
    Empty class.
    """
    def area(self):
        """
        Raise an exception on call.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value type and value and raises error on failure.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
