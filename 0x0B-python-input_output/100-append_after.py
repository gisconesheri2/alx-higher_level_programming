#!/usr/bin/python3
"""inserts a line after each line with a specific string
"""


def append_after(filename="", search="", new_string=""):
    """adds @new_string to @filename after each line
    with the @search term
    """

    all_lines = []

    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp:
            all_lines.append(line)
            if search in line:
                all_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as fp2:
        for line in all_lines:
            fp2.write(line)
