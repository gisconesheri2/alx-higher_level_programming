#!/usr/bin/python3
"""contains a function that checks if an object is exactly
an instance of a specifed class
do not consider inheritance
"""


def is_same_class(obj, a_class):
    """check if obj is an instance of a_class"""
    return (type(obj) is a_class)
