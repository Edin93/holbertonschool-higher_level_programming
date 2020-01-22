#!/usr/bin/python3
""" This module contains a single function.
"""
import json


def load_from_json_file(filename):
    """
    Created an object from a JSON file.
    """

    with open(filename, mode='r') as f:
        file_data = f.read()
        file_to_json = json.dumps(file_data)
        return json.loads(file_to_json)
