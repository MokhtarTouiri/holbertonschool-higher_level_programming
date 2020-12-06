#!/usr/bin/python3
""" Module """


def load_from_json_file(filename):
    """ IMPORT """
    import json
    """ return """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
