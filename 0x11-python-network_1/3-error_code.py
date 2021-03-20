#!/usr/bin/python3
"""
3. Error code #0

"""
from sys import argv
from urllib import error
from urllib import parse
from urllib import request
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
