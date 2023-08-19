#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        ln = (number * -1) % 10
    else:
        ln = (number) % 10
    print(f"{ln}", end="")
    return (ln)
