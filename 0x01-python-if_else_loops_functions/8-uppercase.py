#!/usr/bin/python3


def uppercase(str):
    for let in str:
        if ord(let) > 96 and ord(let) < 123:
            let = chr((ord(let)) - 32)
        print("{}".format(let), end="")
    print()
