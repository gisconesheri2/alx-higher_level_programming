#!/usr/bin/python3
"""prints text with 2 new line added after each of the charcaters:
    '.', '?', ':'
"""


def text_indentation(text):
    """takes text and puts 2 new lines wherever "., :, ?" are found
    Args:
        text (str): string to transform
    Returns:
        Nothing
    """
    pos = 0
    if type(text) != str:
        raise TypeError("text must be a string")

    while pos < len(text):
        char = text[pos]
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            if pos + 1 < len(text):
                if text[pos + 1] == " ":
                    pos += 2
                else:
                    pos += 1
                continue
            else:
                break
        print(char, end="")
        pos += 1
