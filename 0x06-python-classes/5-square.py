#!/usr/bin/python3
""" Module """


class Square:
    """ Empty class """
    def __init__(self, size=0):
        self.size = size
        """ Mokhtar """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)
