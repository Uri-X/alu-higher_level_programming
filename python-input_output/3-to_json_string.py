#!/usr/bin/python3
"""a function that returns JSON representation of an object"""


def to_json_string(my_obj):
    """returns JSON representation of an object"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
