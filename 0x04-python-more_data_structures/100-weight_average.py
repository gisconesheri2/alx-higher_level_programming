#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    total_score = 0
    total = 0

    for score, weight in my_list:
        total_score += (score * weight)
        total += weight

    return (total_score / total)
