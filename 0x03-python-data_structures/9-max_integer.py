#!/usr/bin/python3


def max_integer(my_list=[]):
    biggest_num = 0

    if (len(my_list) == 0):
        return None
    for num in my_list:
        if (num > biggest_num):
            biggest_num = num
    return biggest_num
