#!/usr/bin/python3
"""
Module: type_checker

This module provides functions for type checking in Python.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is an instance of, or if it is an instance of
    a class that inherited from, the specified class `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: Returns `True` if `obj` is an instance of `a_class`
        or its subclass; otherwise returns `False`.
    """
    return isinstance(obj, a_class)
