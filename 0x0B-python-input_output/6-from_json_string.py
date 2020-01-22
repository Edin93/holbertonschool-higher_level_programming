#!/usr/bin/python3
""" This module contains a single function.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by JSON string.
    """
    return json.loads(my_str)
