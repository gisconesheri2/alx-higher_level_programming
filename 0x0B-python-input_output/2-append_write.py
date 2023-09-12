#!/usr/bin/python3
"""writes to a file some text"""


def append_write(filename="", text=""):
    """append text to filename with 'a' mode"""
    with open(filename, mode='a', encoding='utf-8') as fh:
        return (fh.write(text))
