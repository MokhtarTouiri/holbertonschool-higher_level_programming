#!/usr/bin/python3
""" Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ def init """
    def __init__(self, size):
        """ size.self """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
    """ def string """    
    def __str__(self):
        """function 2"""
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string

