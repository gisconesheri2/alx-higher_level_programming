#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as te:
        print(f"Exception: {te}", file=sys.stderr)
        return (False)
    except ValueError as ve:
        print(f"Exception: {ve}", file=sys.stderr)
        return (False)
