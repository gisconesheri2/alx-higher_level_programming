#!/usr/bin/python3
"""do the division of a matrix"""


def matrix_divided(matrix, div):
    """divides each number in the matrix by div
    Args:
        matrix (list of ints/floats): numbers to be divided
        div (int/float): divisor
    Return:
        a new matrix
    """
    new_matrix = []
    row = []
    if len(matrix) == 0:
        raise IndexError("matrix cannot be empty")

    len_of_row = len(matrix[0])

    if len_of_row == 0:
        raise IndexError("matrix cannot be empty")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) == int or type(div) == float:
        for inner_list in matrix:
            if len(inner_list) != len_of_row:
                a = "Each row of the matrix must have the same size"
                raise (TypeError(a))

            for num in inner_list:
                if type(num) == int or type(num) == float:
                    row.append(round(num/div, 2))
                else:
                    first_str = "matrix must be a matrix (list of "
                    second_str = "lists) of integers/floats"
                    raise TypeError(first_str + second_str)
            new_matrix.append(row)
            row = []
    else:
        raise TypeError("div must be a number")

    return (new_matrix)
