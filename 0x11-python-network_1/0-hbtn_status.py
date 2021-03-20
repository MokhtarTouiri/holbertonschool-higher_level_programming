#!/usr/bin/python3
"""
Python script that fetches
"""
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
        read = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(read)))
        print('\t- content: {}'.format(read))
        print('\t- utf8 content: {}'.format(read.decode("utf-8", "replace")))
