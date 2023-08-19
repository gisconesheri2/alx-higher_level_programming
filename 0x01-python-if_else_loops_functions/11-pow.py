#!/usr/bin/python3


def pow(a, b):
    result = 1

    if b == 0:
        return (result)
    elif b > 0:
        for i in range(0, b):
            result = result * a
    else:
        b = b * -1
        for i in range(0, b):
            result = result / a
    return (result)
