#!/usr/bin/python3
""" Module contains single class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class.
    """
    def __init__(self, size):
        """
        Square initialization.
        """
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the square area.
        """
        return self.__size ** 2
