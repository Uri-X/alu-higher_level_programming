#!/usr/bin/python3
"""
function to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class.

    Args:
        obj (any): The object to compare.
        a_class (type): The class to compare with the object.

    Returns:
        bool: `True` if the object is exactly an instance of the
        specified class; otherwise `False`.
    """
    return type(obj) is a_class
