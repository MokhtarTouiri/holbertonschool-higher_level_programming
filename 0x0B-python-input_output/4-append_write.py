#!/usr/bin/python3
""" Module """


def append_write(filename='', text=''):
    """ FileName """
    with open(filename, 'a', encoding='UTF-8') as file:
        """ return """
        return file.write(text)
