#!/usr/bin/python3
""" MODULE """

def say_my_name(first_name, last_name=""):
    """ IF """
    if type(first_name) is not str:
        """ RAISE """
        raise TypeError("first_name must be a string")
    """ IF """
    if type(last_name) is not str:
        """ RAISE """
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")

