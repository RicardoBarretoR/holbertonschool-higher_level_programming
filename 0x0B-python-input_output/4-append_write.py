#!/usr/bin/python3
"""
module 4-append_write that appends a string at the
end of a text file (UTF8) and returns the number of characters added

"""


def append_write(filename="", text=""):
    """
    Function that receives as parameters a file
    and a text to be added to the file

    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        return (f.write(text))
