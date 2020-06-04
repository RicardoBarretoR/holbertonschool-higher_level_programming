#!/usr/bin/python3
"""
module 5-to_json_string that returns the
JSON representation of an object (string

"""
import json


def to_json_string(my_obj):
    'Function that receives an object as a parameter'
    return (json.dumps(my_obj))
