#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0;

    for l1 in matrix:
        for num in l1:
            #print("i is now {}".format(i))
            if (i == 2):
                #print("printing end number")
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end =" ")
            i = i + 1
        i = 0
    if (len(matrix[0]) == 0):
        print()
