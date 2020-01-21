#!/usr/bin/python3
""" Module contains a single class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class.
    """

    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Return the square area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Print message representing the square's dimensions.
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
