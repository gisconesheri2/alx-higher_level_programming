#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square module for everything
"""


class Square:
    """ defines a square. """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize the data
        Args:
            position (tuple(int, int)): offset to print square
            size (int): dimensions of the square

        Attributes:
            position (tuple(int, int)): offset to print square
            size: dimensions of the square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, val):
        """sets the value of position offset
        Args:
            val (tuple(int, int)): offset for printing the square
        """
        if len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(val[0]) != int or type(val[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

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
        """print a square using '#'"""
        if self.__size == 0:
            return
        for line_space in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for line in range(self.__position[0]):
                print(" ", end="")
            for char in range(self.__size):
                print("#", end="")
            if row == self.__size - 1:
                continue
            print()

    def __str__(self):
        """Implement the __str__ magic function"""
        self.my_print()
        return ("")
