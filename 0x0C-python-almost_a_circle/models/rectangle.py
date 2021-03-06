#!/usr/bin/python3
"""
module "rectangle" that inherits from Base

"""
from models.base import Base


class Rectangle(Base):
    'create class rectangle'
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        'returns value of attribute, width'
        return self.__width

    @width.setter
    def width(self, value):
        'sets value of attribute'
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        'returns value of attribute, height'
        return self.__height

    @height.setter
    def height(self, value):
        'sets value of attribute'
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        'returns value of attribute, x'
        return self.__x

    @x.setter
    def x(self, value):
        'sets value of attribute'
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        'return value of attribute, y'
        return self.__y

    @y.setter
    def y(self, value):
        'sets value of attribute'
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        'returns the area value of the Rectangle instance'
        return self.width * self.height

    def display(self):
        'prints in stdout the Rectangle instance with char #'
        for colum in range(self.y):
            print()

        for i in range(self.height):
            for row in range(self.x):
                print(' ', end='')

            for j in range(self.width):
                print('#',  end='')
            print()

    def __str__(self):
        'redefine the method and return the string'
        return ("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        'assigns an argument to each attribute'
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.width = kwargs['width']
                    if i == 'height':
                        self.height = kwargs['height']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        'function that returns the dictionary representation of a Rectangle'
        dic_rectangle = {
            'width': self.width,
            'height': self.height,
            'id': self.id,
            'x': self.x,
            'y': self.y
        }

        return dic_rectangle
