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
        for i in range(self.height):
            for j in range(self.width):
                print('#',  end='')
            print()
