#!/usr/bin/python3
"""
2. POST an email #0

"""
from sys import argv
from urllib import parse
from urllib import request
if __name__ == "__main__":
    value = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], value) as response:
        print(response.read().decode('utf-8'))
