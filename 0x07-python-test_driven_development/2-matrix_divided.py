#!/usr/bin/python3
""" Module """


def matrix_divided(matrix, div):
    """ IF """
    if len(matrix) == 0:
        """ RAISE """
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    """ IF """
    if type(matrix) is not list:
        """ RAISE """
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    """ IF """
    if div == 0:
        """ RAISE """
        raise ZeroDivisionError("division by zero")
    """ IF """
    if not isinstance(div, (int, float)):
        """ RAISE """
        raise TypeError("div must be a number")
    """ FOR """
    for a in matrix:
        """ IF """
        if len(a) != len(matrix[0]):
            """ RAISE """
            raise TypeError("Each row of the matrix" +
                            "must have the same size")
        """ IF """
        if type(a) is not list or len(a) == 0:
            """ IF """
            raise TypeError("matrix must be a matrix" +
                            "(list of lists) of integers/floats")
        """ FOR """
        for i in a:
            """ IF """
            if not isinstance(i, (int, float)):
                """ RAISE """
                raise TypeError("matrix must be a matrix" +
                                "(list of lists)of integers/floats")
    return [[round(i / div, 2) for i in a] for a in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
