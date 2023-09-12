#!/usr/bin/python3
""" returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """return dict description of obj to allow for JSON serialization"""
    instance_dict = vars(obj)
    class_attrs = vars(obj.__class__)
    for k, v in class_attrs.items():
        if k[0:2] == "__":
            continue
        if type(v) is int or type(v) is str or type(v) is dict:
            instance_dict[k] = v
        if type(v) is bool or type(v) is list:
            instance_dict[k] = v
    return instance_dict
