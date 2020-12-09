#!/usr/bin/python3
""" MODULE """


def print_square(size):
    """ IF """
    if type(size) is not int:
        """ RAISE """
        raise TypeError("size must be an integer")
    """ IF """
    if size < 0:
        """ RAISE """
        raise ValueError("size must be >= 0")
    """ IF """
    if type(size) is float and size < 0:
        """ RAISE """
        raise TypeError("size must be an integer")
    print((("#" * size + "\n") * size), end="")
""" IF """
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
