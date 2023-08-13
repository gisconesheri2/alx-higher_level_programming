#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = []
    i = 0

    if (idx < 0 or idx >= len(my_list)):
        for num in my_list:
            new_list.append(num)
        return new_list
    else:
        for num in my_list:
            if (i == idx):
                new_list.append(element)
                i += 1
                continue
            new_list.append(num)
            i += 1
    return new_list
