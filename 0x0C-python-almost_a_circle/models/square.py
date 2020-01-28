#!/usr/bin/python3
"""
This module contains a single Square class. it inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle and makes a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        args = [self.id, self.x, self.y, self.height]
        return '[Square] ({0}) {1}/{2} - {3}'.format(*args)

    @property
    def size(self):
        """
        Returns the square size.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the square size value.
        """
        self.width = size
        self.height = size
