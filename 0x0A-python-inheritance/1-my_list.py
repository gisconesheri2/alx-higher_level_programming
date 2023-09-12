#!/usr/bin/python3
"""prints out a sorted list to stdout
"""


class MyList(list):
    """inherits from list and contains a method to
    print out a list in sorted ascending order
    """

    def print_sorted(self):
        """prints a copy of the MyList object sorted
        in ascending order
        """
        nl = self.copy()
        nl.sort()
        print(nl)
