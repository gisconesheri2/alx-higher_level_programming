#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_nums = set(my_list)
    total = 0

    for num in unique_nums:
        total = total + num
    return (total)
