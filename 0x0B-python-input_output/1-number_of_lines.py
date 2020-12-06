#!/usr/bin/python3
""" Module """


def number_of_lines(filename=""):
    """ Filename """
    with open(filename, "r", encoding="UTF-8") as f:
        """ return """
        return len(f.readlines())
