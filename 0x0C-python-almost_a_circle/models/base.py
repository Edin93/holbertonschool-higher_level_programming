#!/usr/bin/python3
"""
This module contains a single class, called Base.
"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        list = []
        fn = cls.__name__ + '.json'
        try:
            with open(fn, 'r') as f:
                data = cls.from_json_string(f.read())
            for dict in data:
                list.append(cls.create(**dict))
            return list
        except:
            return list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialiezes to CSV.
        """
        fn = cls.__name__ + '.csv'
        objs = []
        with open(fn, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            if list_objs is not None:
                for obj in list_objs:
                    l = []
                    x = obj.x
                    y = obj.y
                    id = obj.id
                    if cls.__name__ == 'Square':
                        size = obj.size
                        l = [id, size, x, y]
                    else:
                        height = obj.height
                        width = obj.width
                        l = [id, width, height, x, y]
                    objs.append(l)
            for obj in objs:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes from CSV.
        """
        list = []
        fn = cls.__name__ + '.csv'
        try:
            with open(fn, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if cls.__name__ == 'Square':
                        d = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                    else:
                        d = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    list.append(cls.create(**d))
            return list
        except:
            return list
