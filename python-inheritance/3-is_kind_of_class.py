#!/usr/bin/python3
"""
Module: my_module

This module contains functions for type checking in Python.
"""

def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class.

    Args:
        obj (any): The object to compare.
        a_class (any): The class to compare with the object.

    Returns:
        bool: `True` if the object is exactly an instance of the
        specified class; otherwise `False`.
    """
    return type(obj) == a_class
