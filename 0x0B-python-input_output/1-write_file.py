#!/usr/bin/python3
"""writes to a file some text"""


def write_file(filename="", text=""):
    """write text to filename with 'w' mode"""
    with open(filename, mode='w', encoding='utf-8') as fh:
        return (fh.write(text))
