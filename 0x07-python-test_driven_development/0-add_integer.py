#!/usr/bin/python3
"""Args:
    a (int/float): first number
    b (int/float): second number
Return:(int) sum of a and b
"""


def add_integer(a, b=98):
    """adds two numbers that must be integers or floats
    TypeError raised if above is not met
    floats are casted to int before computation"""

    if type(a) == int or type(a) == float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) == int or type(b) == float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return (a + int(b))
