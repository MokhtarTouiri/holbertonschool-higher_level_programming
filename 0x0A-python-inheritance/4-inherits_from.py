#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """ If """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        """ Return True """
        return True
    else:
        """ Return False """
        return False
