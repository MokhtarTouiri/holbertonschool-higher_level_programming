#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Filename """
    with open(filename, "r", encoding="UTF-8") as file:
        ready = file.read()
    print(ready, end="")
