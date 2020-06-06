#!/usr/bin/python3
"""
module 'text_indentation' that prints a text with 2
new lines after each of these characters: ., ? and

"""


def text_indentation(text):
    'function that receive as parameter a text only type string'
    if type(text) != str:
        raise TypeError("text must be a string")

    for i in text:
        if i not in '.?:':
            print(i, end='')
        else:
            print(i)
            print()
