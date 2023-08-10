#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argl = sys.argv
    num = 1
    arg_length = len(argl)

    if (arg_length == 1):
        print("0 arguments.")

    elif (arg_length == 2):
        print("1 argument:")
        print("1: {}".format(argl[1]))

    else:
        print("{} arguments:".format(arg_length - 1))
        for arg in argl[1:]:
            print("{}: {}".format(num, arg))
            num = num + 1
