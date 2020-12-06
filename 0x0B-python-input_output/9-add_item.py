#!/usr/bin/python3
""" Module """


import os.path
from sys import argv
""" Module """
save_j = __import__("7-save_to_json_file").save_to_json_file
load_j = __import__("8-load_from_json_file").load_from_json_file
list_j = []
try:
    """ list_j """
    list_j = load_j("add_item.json")
except Exception:
    """ list_j """
    list_j = []
for argument in argv[1:]:
    """ list_j """
    list_j.append(argument)
save_j(list_j, "add_item.json")
