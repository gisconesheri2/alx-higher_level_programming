#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for let in my_string:
        if (let == "C") or (let == "c"):
            continue
        new_string = new_string + let
    return new_string
