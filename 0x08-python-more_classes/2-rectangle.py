#!/usr/bin/python3
"""Models a rectangle
"""


class Rectangle:
    """models a rectangle
    """

    def __init__(self, width=0, height=0):
        """initialize the object
        Args:
            width (int): width of rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute
        Args:
            value (int): value supplied for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the width attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for width attribute
        Args:
            value (int): value supplied for width
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """calculates and returns the pereimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return (0)
        else:
            return ((self.width * 2) + (self.height * 2))
