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
    def to_json(self, attrs=None):
        if attrs is None:
            """ RETURN SELF """
            return self.__dict__
        d = {}
        for x in attrs:
            """ IF """
            if x in self.__dict__:
                d[x] = self.__dict__[x]
        """ Return d """
        return d
    """ DEF RELOAD """
    def reload_from_json(self, json):
        for keys, value in json.items():
            self.__dict__[keys] = value
