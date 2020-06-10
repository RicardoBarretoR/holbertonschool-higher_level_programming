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

    def update(self, *args, **kwargs):
        'function that assigns attributes'
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary representation of square """
        square_dict = {}
        square_attrs = ["id", "size", "x", "y"]
        for attr in square_attrs:
            square_dict[attr] = getattr(self, attr)
        return square_dict
