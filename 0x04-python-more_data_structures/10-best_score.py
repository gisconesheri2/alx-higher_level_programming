#!/usr/bin/python3


def best_score(a_dictionary):
    best = None
    big = 0

    if a_dictionary is None:
        return (best)

    for k, v in a_dictionary.items():
        if v > big:
            big = v
            best = k
    return (best)
