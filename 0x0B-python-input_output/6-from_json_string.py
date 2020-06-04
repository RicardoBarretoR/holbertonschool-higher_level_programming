#!/usr/bin/python3
"""
module 6-from_json_string  that returns an object
(Python data structure) represented by a JSON string

"""
import json


def from_json_string(my_str):
    'Function that receives an object as a parameter'
    return (json.loads(my_str))
