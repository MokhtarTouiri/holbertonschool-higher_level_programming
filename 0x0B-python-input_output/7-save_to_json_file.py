#!/usr/bin/python3
""" Module """


def save_to_json_file(my_obj, filename):
    """ IMPORT """
    import json
    """ return """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
