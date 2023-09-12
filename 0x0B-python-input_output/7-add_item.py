#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""adds all arguments to a python list and saves them to a json file"""


args = sys.argv[1:]
py_list = []
filename = 'add_item.json'
try:
    try:
        py_list = load_from_json_file(filename)
    except json.decoder.JSONDecodeError:
        empty_list = []
        save_to_json_file(empty_list, filename)
except FileNotFoundError:
    empty_list = []
    save_to_json_file(empty_list, filename)

if len(args) == 0:
    save_to_json_file(py_list, filename)
else:
    for arg in args:
        py_list.append(arg)
    save_to_json_file(py_list, filename)
