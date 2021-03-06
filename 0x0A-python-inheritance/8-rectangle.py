#!/usr/bin/python3
""" This module contains a single class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Simple Rectangle class.
    """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__height = height
        self.__width = width
