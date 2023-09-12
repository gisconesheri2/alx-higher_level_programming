#!/usr/bin/python3
"""return a list of lists of integers representing
the pascal's triangle of n
"""


def pascal_triangle(n):
    """return a pascal triangle of size n"""
    pascal_list = []
    inner_list = []

    if n <= 0:
        return (pascal_list)

    pascal_list.append([1])
    if n == 1:
        return pascal_list

    pascal_list.append([1, 1])
    if n == 2:
        return pascal_list

    for ol in range(2, n):
        inner_list.append(1)
        upper_list = pascal_list[ol-1]
        for il in range(0, ol-1):
            inner_list.append(upper_list[il] + upper_list[il + 1])
        inner_list.append(1)
        pascal_list.append(inner_list)
        inner_list = []

    return pascal_list
