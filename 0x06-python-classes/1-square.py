#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square module for everything
"""


class Square:
    """ defines a square. """

    def __init__(self, size):
        """ initialize the data
        Args:
            size (int): dimensions of the square

        Attributes:
            size: dimensions of the square
        """
        self.__size = size
