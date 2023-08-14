#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0
    inner_len = 0

    for l1 in matrix:
        inner_len = len(l1)
        if (inner_len == 0):
            print()
            break
        while (i < inner_len - 1):
            print("{:d}".format(l1[i]), end=" ")
            i = i + 1
        print("{:d}".format(l1[i]))
        i = 0
