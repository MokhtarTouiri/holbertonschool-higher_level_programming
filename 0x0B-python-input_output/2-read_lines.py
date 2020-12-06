#!/usr/bin/python3
""" Module """


def read_lines(filename="", nb_lines=0):
    """ FileName """
    with open(filename, "r", encoding="UTF-8") as f:
        """ IF """
        if nb_lines <= 0:
            print(f.read(), end="")

        else:
            for l in f:
                print(l, end="")
