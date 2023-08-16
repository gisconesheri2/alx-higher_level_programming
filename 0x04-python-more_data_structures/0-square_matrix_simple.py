#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = []
    inner_row = []

    square_matrix = [[num * num for num in row]for row in matrix]
    """
    for row in matrix:
        for num in row:
            inner_row.append(num * num)
        square_matrix.append(inner_row)
        inner_row = []
    """

    return(square_matrix)
