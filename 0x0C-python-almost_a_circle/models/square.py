#!/usr/bin/python3
"""
module 'Square' that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    'Class Square inherits from Rectangle'
    def __init__(self, size, x=0, y=0, id=None):
        'class constructor'

        super().__init__(size, size, x, y, id)

    def __str__(self):
        'string represntacion of a square'
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        'return value of attribute, size'
        return self.width

    @size.setter
    def size(self, value):
        'sets value of attribute'
        self.width = value
        self.height = value
