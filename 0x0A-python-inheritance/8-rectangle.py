#!/usr/bin/python3
"""contains a empty class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines Rectangle template
    inherits rom BaseGeometry parent
    """

    def __init__(self, width, height):
        """initialize the object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
