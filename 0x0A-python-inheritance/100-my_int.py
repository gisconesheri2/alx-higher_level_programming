#!/usr/bin/python3
"""inverses the == and != operators for ints"""


class MyInt(int):
    """== and != operators are inverted"""

    def __eq__(self, second_num):
        """invert the == operator"""
        if self / second_num  == 1:
            return False 
        return True

    def __ne__(self, second_num):
        """invert the != operator"""
        if self == second_num:
            return False
        return True
