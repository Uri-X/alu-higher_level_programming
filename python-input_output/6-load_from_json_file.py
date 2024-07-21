#!/usr/bin/python3
"""a function that creates an object from a JSON file"""


def load_from_json_file(filename):
    """creates object from JSON representation in file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
