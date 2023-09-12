#!/usr/bin/python3
import json
"""generates a python object from a json string"""


def from_json_string(my_str):
    """return a python object from a json string"""
    return (json.loads(my_str))
