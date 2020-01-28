#!/usr/bin/python3
"""
This module contains a single class, called Base.
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of the given argument.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
