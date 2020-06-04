#!/usr/bin/python3
"""
module number_of_lines returns
the number of lines of a text file

"""


def number_of_lines(filename=""):
    'Function that receives as a parameter a file'

    numl = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            numl += 1
    return numl
