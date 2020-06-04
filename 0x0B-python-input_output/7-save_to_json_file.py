#!/usr/bin/python3
"""
module 7-save_to_json_file that writes an Object
to a text file, using a JSON representation

"""
import json


def save_to_json_file(my_obj, filename):
    'Function that receives as parameters a text file and an object'
    with open(filename, mode='w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
