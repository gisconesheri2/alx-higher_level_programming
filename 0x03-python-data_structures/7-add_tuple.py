#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    idx = 0
    sum_0 = 0
    sum_1 = 0

    while (idx < 2):
        if (len(tuple_a) == 1):
            tuple_a = tuple_a + (0, )
        if (len(tuple_b) == 1):
            tuple_b = tuple_b + (0, )
        if (len(tuple_a) == 0):
            tuple_a = (0, 0)
        if (len(tuple_b) == 0):
            tuple_b = (0, 0)
        sum_0 = tuple_a[0] + tuple_b[0]
        sum_1 = tuple_a[1] + tuple_b[1]
        idx += 1
    return (sum_0, sum_1)
