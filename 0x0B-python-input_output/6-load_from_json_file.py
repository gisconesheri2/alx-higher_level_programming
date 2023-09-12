#!/usr/bin/python3
import json
"""creats an Object from a JSON file"""


def load_from_json_file(filename):
    """return a python object from a json file"""
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)
