#!/usr/bin/python3
"""
module 2-read_lines reads n lines of
a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    """
    Function that receives as parameters a
    file and the number of lines of the text to be printed

    """
    n = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            if n < nb_lines or nb_lines <= 0:
                print(line, end='')
                n += 1
