#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square module for everything
"""


class Square:
    """ defines a square. """

    def __init__(self, size=0):
        """ initialize the data
        Args:
            size (int): dimensions of the square

        Attributes:
            size: dimensions of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")
        self.__size = size

    def area(self):
        """calculates the area of the square
        Returns:
            int: area of the square
        """
        return (self.__size * self.__size)
