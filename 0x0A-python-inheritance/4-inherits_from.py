#!/usr/bin/python3
"""checks if an object is an instance of class that
 inherits for a specific a_class either directly of indirectly
"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class
    that inherits from a_class
    """
    if type(obj) is a_class:
        return False
    return (issubclass(type(obj), a_class))
