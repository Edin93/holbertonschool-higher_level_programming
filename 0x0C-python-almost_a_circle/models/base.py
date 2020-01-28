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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of the given argument.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representationt of list_objs to a file.
        """
        list = []
        if list_objs is None or len(list_objs) == 0:
                return cls.to_json_string(list)
        else:
            fn = str(type(list_objs[0]).__name__) + '.json'
            for inst in list_objs:
                list.append(inst.to_dictionary())
            with open(fn, 'w') as f:
                f.write(cls.to_json_string(list))
