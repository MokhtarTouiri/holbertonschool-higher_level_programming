#!/usr/bin/python3
""" Module """


class Student:
    """ DEF INIT """
    def __init__(self, first_name, last_name, age):
        """ SELF """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    """ DEF JSON """
    def to_json(self):
        """ RETURN SELF """
        return self.__dict__
