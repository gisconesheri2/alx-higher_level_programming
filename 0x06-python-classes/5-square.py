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

    @property
    def size(self):
        """retrieve the value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the value of size to value

            Args:
                value (int): value of size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must >= 0")
        self.__size = value

    def area(self):
        """calculates the area of the square
        Returns:
            int: area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """print a square using '#'
        """
        if self.__size == 0:
            print()
        for line in range(self.__size):
            for char in range(self.__size):
                print("#", end="")
            print()
