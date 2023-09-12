#!/usr/bin/python3
"""opens a file and reads all lines into the stdout
"""


def read_file(filename=""):
    """opens a file and reads all lines into the stdout
    """
    with open(filename, 'r', encoding='utf-8') as fhandle:
        for line in fhandle:
            print(line.rstrip())
