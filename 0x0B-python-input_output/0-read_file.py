#!/usr/bin/python3
"""
module read_file reads a text file
(UTF8) and prints it to stdout

"""


def read_file(filename=""):
    'unctiFon prototype that has a'
    'ile as an input parameter'
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
