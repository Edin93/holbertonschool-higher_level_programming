#!/usr/bin/python3
""" This module contains a single function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write JSON representation of my_obj in file (filename).
    """

    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
