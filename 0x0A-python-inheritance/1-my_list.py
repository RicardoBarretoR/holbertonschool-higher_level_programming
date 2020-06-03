#!/usr/bin/python3
"""
class Mylist that inherits from list

"""


class MyList(list):
    'subclass'

    def print_sorted(self):

        print(sorted(self))
