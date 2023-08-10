#!/usr/bin/python3

import calculator_1 as ped

a = 10
b = 5

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, ped.add(a, b)))
    print("{} - {} = {}".format(a, b, ped.sub(a, b)))
    print("{} * {} = {}".format(a, b, ped.mul(a, b)))
    print("{} / {} = {}".format(a, b, ped.div(a, b)))
