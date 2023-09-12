#!/usr/bin/python3
"""returns the list of available attributes
and methods available for the object
"""


def lookup(obj):
    """returns the list of available attributes
    and methods available for the object
    """
    return (dir(obj))
