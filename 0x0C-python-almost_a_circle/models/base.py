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
        fn = cls.__name__ + '.json'
        if list_objs is not None:
            for inst in list_objs:
                list.append(inst.to_dictionary())
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON strin representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returs an instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dum = cls(10, 10)
        elif cls.__name__ == 'Square':
            dum = cls(10)
        dum.update(**dictionary)
        return dum
