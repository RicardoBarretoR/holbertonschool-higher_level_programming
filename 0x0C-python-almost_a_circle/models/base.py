#!/usr/bin/python3
"""
module "base" The goal of it is to manage id attribute in
all your future classes and to avoid duplicating the same code

"""
import json


class Base:
    'The base class is created'
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return'[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dictionaries = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())
        json_string = Base.to_json_string(list_dictionaries)
        with open("{}.json".format(cls.__name__), mode='w', encoding='UTF-8')\
                as f:
            f.write(json_string)
