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

    def area(self):
        """return the area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """return the object type as weel as height and width"""
        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")
