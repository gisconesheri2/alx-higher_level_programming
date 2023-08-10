#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argl = sys.argv
    total = 0
    arg_length = len(argl)

    if (arg_length == 1):
        print(total)

    else:
        for arg in argl[1:]:
            total = total + int(arg)
        print(total)
