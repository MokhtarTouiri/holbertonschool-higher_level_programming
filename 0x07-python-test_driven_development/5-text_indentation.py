#!/usr/bin/python3
""" MODULE """


def text_indentation(text):
    """ IF """
    if type(text) != str:
        """ RAISE """
        raise TypeError("text must be a string")
    for x in ".?:":
        text = (x + "\n\n").join(
            [y.strip(" ")for y in text.split(x)])
    print(text, end="")
""" IF """
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

