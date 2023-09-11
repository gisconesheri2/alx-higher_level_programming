#!/usr/bin/python3
"""checks if an object is an instance of class that
 inherits for a specific a_class either directly of indirectly
"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class
    that inherits from a_class
    """
    return (issubclass(type(obj), a_class))
