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
    ip = float('inf')
    im = float('inf')
    if not isinstance(div, (int, float)) or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == ip or div == im:
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    if len(matrix) == 0 or len(matrix[0]) == 0:
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
            if (
                    not isinstance(matrix[li][ei], (int, float))
                    or matrix[li][ei] == ip or matrix[li][ei] == im
                    or matrix[li][ei] != matrix[li][ei]
            ):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            new[li].append(round(matrix[li][ei] / div, 2))
    return new


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/2-matrix_divide.txt')
