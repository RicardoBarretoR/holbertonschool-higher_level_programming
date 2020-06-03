#!/usr/bin/python3
"""
module that contains one function: lookup

"""


def lookup(obj):
    'returns the list of available attributes and methods of an object'
    return dir(obj)
