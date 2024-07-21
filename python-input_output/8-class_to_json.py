#!/usr/bin/python3
"""defines function to return dictionary description with data structure"""


def class_to_json(obj):
    """returns dictionary description for JSON serialization"""
    return obj.__dict__
