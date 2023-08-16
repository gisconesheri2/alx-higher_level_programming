#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))

    for k in keys:
        print("{}: {}".format(k, a_dictionary[k]))
