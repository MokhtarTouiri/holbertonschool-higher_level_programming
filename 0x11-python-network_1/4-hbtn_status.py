#!/usr/bin/python3
"""4. What's my status? #1
"""
import requests
if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(
        type(response.text), response.text))
