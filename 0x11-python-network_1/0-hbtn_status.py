#!/usr/bin/python3
""" Python script that fetches """


if __name__ == "__main__":
    from ullib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        read = response.read()
        print('Body response:')
        print('\t- content: {}'.format(read))
        print('\t- type: {}'.format(type(read)))
        print('\t- utf8 content: {}'.format(read.decode("utf-8", "replace")))
