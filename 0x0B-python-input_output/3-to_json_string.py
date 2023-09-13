#!/usr/bin/python3
"""convert a python object into a json representtion"""
import json


def to_json_string(my_obj):
    """encodes a python object into a json represeantaion"""
    return (json.dumps(my_obj))
