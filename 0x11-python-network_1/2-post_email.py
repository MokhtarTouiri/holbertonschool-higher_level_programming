#!/usr/bin/python3
"""
2. POST an email #0

"""
from sys import argv
from urllib import parse
from urllib import request
if __name__ == "__main__":
    values = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], values) as response:
        print(response.read().decode('utf-8'))
