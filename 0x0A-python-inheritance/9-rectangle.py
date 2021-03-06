#!/usr/bin/python3
""" This module contains a single class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Simple Rectangle class.
    """
    def __init__(self, width, height):
        """
        Initialization of rectangle.
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        Return rectangle area.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        print rectangle message.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
