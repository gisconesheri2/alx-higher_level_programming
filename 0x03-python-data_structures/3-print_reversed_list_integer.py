#!/usr/bin/python3


def print_reversed_list_integer(my_list):
    if my_list is not None:
        length = len(my_list) - 1
        while (length >= 0):
            print("{:d}".format(my_list[length]))
            length = length - 1
