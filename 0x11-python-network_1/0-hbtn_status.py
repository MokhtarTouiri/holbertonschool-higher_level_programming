#!/usr/bin/python3
"""
0. What's my status? #0
"""
from urllib import request
if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
