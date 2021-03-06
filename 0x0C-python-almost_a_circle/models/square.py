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

    def update(self, *args, **kwargs):
        """
        Update the square instance.
        """
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                    setattr(self, k, v)
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.height = args[1]
                    self.width = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

    def to_dictionary(self):
        """
        Returns the dictionary representations of a Square.
        """
        d = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return d
