#!/usr/bin/python3
"""
module 3-write_file that writes a string to a text
file (UTF8) and returns the number of characters written

"""


def write_file(filename="", text=""):
    """
    Function that receives as parameter a
    file and a text to write in the file

    """
    with open(filename, mode='w', encoding='UTF-8') as f:
        return (f.write(text))
