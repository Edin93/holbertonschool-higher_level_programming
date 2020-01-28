#!/usr/bin/python3
"""
This module contains a single class, Rectangle.
"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """
        Returns the instance's height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the instance's height value.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        """
        Returns the instance widht.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the instance width value.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def x(self):
        """
        Returns the instance x value.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the instance's x value.
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Returns the instance's y value.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the instance y value.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the rectangle's area.
        """
        return self.height * self.width

    def display(self):
        """
        Prints in stdout the Rectangle instance with the # character.
        """
        for y in range(self.y):
            print()
        for line in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Returns a string represing the Rectangle's instance.
        """
        args = [self.id, self.x, self.y, self.width, self.height]
        return '[Rectangle] ({0}) {1}/{2} - {3}/{4}'.format(*args)

    def update(self, *args, **kwargs):
        """
        Update the rectangle's attribute values from array args.
        """
        for i in range(len(args)):
            if i == 0:
                super().__init__(args[0])
            if i == 1:
                self.width = args[1]
            if i == 2:
                self.height = args[2]
            if i == 3:
                self.x = args[3]
            if i == 4:
                self.y = args[4]

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.
        """
        d = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height}
        d['width'] = self.width
        return d
