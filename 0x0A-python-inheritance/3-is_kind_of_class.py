#!/usr/bin/python3
"""checks if an object is an instance of a specific a_class
also checks for inheritance
"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a specific a_class
    also checks for inheritance if a_class is a subclass
    """
    return (isinstance(obj, a_class))
