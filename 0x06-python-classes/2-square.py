#!/usr/bin/python3
""" Module """


class Square:
    """ Empty Class """
    def __init__(self, size=0):
        """ Mokhtar """
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
