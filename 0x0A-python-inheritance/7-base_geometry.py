#!/usr/bin/python3
"""contains a empty class BaseGeometry
"""


class BaseGeometry(object):
    """an empty class that inherits from object"""

    def area(self):
        """calculate area of a grometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an int greater than 0
        Args:
            name (str): identifier for the value
            value (int):
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
