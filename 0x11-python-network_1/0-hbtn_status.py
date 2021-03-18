#!/usr/bin/python3
""" Python script that fetches """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        read = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(read), read, read.decode('utf-8')))
