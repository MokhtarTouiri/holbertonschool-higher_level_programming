#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Filename """
    with open(filename, "r", encoding="UTF-8") as f:
        ready = f.read()
    print(ready, end="")
