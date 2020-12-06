#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """ pass """
    def area(self):
        """ is not implemented """
        raise Exception('area() is not implemented')
    """ def int """
    def integer_validator(self, name, value):
        if type(value) is not int:
            """ must be a integer """
            raise TypeError('<name> must be an integer')
        if value <= 0:
            """ must be greater """
            raise ValueError('<name> must be greater than 0')
        if type(name) is not str:
            """ must be string """
            raise TypeError('{} must be a string'.format(name))
""" Module """
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
