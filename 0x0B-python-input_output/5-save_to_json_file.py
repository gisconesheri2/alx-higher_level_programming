#!/usr/bin/python3
"""writes a json_string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes to filename the json string representation of my_obj
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
