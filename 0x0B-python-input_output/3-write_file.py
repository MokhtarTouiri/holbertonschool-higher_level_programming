#!/usr/bin/python3
""" Module """


def write_file(filename="", text=""):
    """ FileName """
    with open(filename, "w", encoding="UTF-8") as file:
        """ return """
        return file.write(text)
