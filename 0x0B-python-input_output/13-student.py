#!/usr/bin/python3
""" This module contains a single class.
"""


class Student:
    """
    Student class defined by first and last name and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Init Student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retreive dictionary representation of a student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for item in attrs:
                for k in self.__dict__:
                    if k == item:
                        dic[k] = self.__dict__[k]
            return dic

    def reload_from_json(self, json):
        if len(json) > 0:
            for k in json:
                self.__dict__[k] = json[k]
