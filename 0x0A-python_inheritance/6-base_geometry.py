#!/usr/bin/python3
"""contains a empty class BaseGeometry
"""


class BaseGeometry(object):
    """an empty class that inherits from object"""

    def area(self):
        """calculate area of a grometric shape"""
        raise Exception("area() is not implemented")
