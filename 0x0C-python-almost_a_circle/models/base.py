#!/usr/bin/python3
"""
This module contains a single class, called Base.
"""


class Base():
    """
    Base class for all the other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
