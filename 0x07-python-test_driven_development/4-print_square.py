#!/usr/bin/python3
"""prints a square given a certain dimension"""


def print_square(size):
    """prints a square with the character '#'
    Args:
        size (int): dimension of the square
                    must be a positive integer
    Returns: nothing
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0 and type(size) == float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print("")
