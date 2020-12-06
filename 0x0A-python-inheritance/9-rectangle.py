#!/usr/bin/python3
""" Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ def init """
    def __init__(self, width, height):
        """ is not implemented """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
    """ def area """
    def area(self):
        """ return self """
        return self.__width * self.__height
    """ def str """
    def __str__(self):
        """ string """
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        """ return self """
        return string
