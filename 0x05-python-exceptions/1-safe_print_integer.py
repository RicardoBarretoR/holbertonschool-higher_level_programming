#!/usr/bin/python3
def safe_print_integer(value):
    """"prints an integer with "{:d}".format()"""
    try:
        if value % 1 == 0:
            print("{:d}".format(value))
        return True
    except TypeError:
        return False
