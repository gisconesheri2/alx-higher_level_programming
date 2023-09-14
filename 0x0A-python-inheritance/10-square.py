#!/usr/bin/python3
"""contains a empty class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square type"""

    def __init__(self, size):
        """initialize a Square object
        """
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """get the area of the Square"""
        return (self.__size * self.__size)
