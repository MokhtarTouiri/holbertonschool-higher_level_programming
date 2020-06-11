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
        if type(value) != int:
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """ Area """
    def area(self):
        return self.__height * self.__width
    """ Mokhtar """
    def perimeter(self):
        return (self.__height + self.__width) * 2
    """ Str """
    def __str__(self):
        """ Mokhtar """
        a = ""
        if self.__height is 0:
            return a
        for i in range(self.__height - 1):
            a += '#' * self.__width + '\n'
        a += '#' * self.__width
        return a
    """ Mokhtar """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__height, self.__width)
