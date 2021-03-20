#!/usr/bin/python3
"""9. My GitHub!
"""
from requests import get
import sys
if __name__ == '__main__':
    X = get('https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2])).json()
    print(X.json().get('id'))
