#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our matrix_divided function module, Ex:
>>> matrix = [
... [1, 2, 3],
... [4, 5, 6]
... ]
>>> [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divides elements of the matrix by div.
    """
    if div is None:
        raise TypeError("div must be a number")
    if not type(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
        floats")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
        floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
        floats")
    ln = 0
    if isinstance(matrix, list):
        ln = len(matrix[0])
    new = []
    for li in range(len(matrix)):
        if not isinstance(matrix[li], list):
            raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
        if len(matrix[li]) != ln:
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for ei in range(len(matrix[li])):
            if not type(l[ei], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            new[li].append(round(matrix[li][ei] / div, 2))
    return new
