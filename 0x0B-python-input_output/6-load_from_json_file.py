#!/usr/bin/python3
"""creats an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """return a python object from a json file"""
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)
