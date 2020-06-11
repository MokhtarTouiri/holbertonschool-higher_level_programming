#!/usr/bin/python3
""" Module """


class Rectangle:
    """ Mokhtar """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """ Mokhtar """
    @property
    def width(self):
        return self. __width
    """ Mokhtar """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """ Mokhtar """
    @property
    def height(self):
        return self.__height
    """ Mokhtar """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
