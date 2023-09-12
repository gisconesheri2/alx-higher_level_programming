#!/usr/bin/python3
import json
"""convert a python object into a json representtion"""


def to_json_string(my_obj):
    """encodes a python object into a json represeantaion"""
    return (json.dumps(my_obj))
