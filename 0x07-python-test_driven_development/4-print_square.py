#!/usr/bin/python3
"""
module 'print_square' print a square with the character #

"""


def print_square(size):
    """
    function that receives as a parameter
    the size length of the square

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
