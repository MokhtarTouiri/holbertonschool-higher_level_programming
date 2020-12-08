#!/usr/bin/python3
""" MODULE """


def add_integer(a, b=98):
    """ IF """
    if type(a) is not float and type(a) is not int:
        """ TYPE ERROR """
        raise TypeError('a must be an integer')
    """ IF """
    if type(b) is not float and type(b) is not int:
        """ TYPE ERROR """
        raise TypeError('b must be an integer')
        b = int(b)
        a = int(a)
    """ RETURN """
    return (a + b)
""" IF """
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
