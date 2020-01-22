#!/usr/bin/python3
""" This module contains a single function.
"""
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if os.path.isfile('add_item.json'):
    data = load_from_json_file('add_item.json')
    if (len(sys.argv) >= 2):
        for i in range(1, len(sys.argv)):
            data.append(str(sys.argv[i]))
        save_to_json_file(data, 'add_item.json')
else:
    save_to_json_file([], 'add_item.json')
