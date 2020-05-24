#!/usr/bin/python3
"""
This is the "Matrix Divided" module.

The Matrix Divided module takes in a list of lists matrix and divisor.
All valid elements are divided by the divisor and returned as new matrix.

"""


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix.'''

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    size_m = 0
    for elem in matrix:
        if size_m is 0:
            size_m = len(elem)
        elif size_m != len(elem):
            raise TypeError('Each row of the matrix must have the same size')

        for j in elem:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of'
                    ' integers/floats')
    return [[round(i / div, 2) for i in elem] for elem in matrix]
