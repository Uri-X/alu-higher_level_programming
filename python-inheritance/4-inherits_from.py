#!/usr/bin/python3
"""
Module: type_checker

This module provides functions for type checking in Python.
"""


def inherits_from(obj, a_class):
    """
    Checks if `obj` is an instance of a class that inherited
    (directly or indirectly) from the specified class `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: Returns `True` if `obj` is an instance of a class
        that inherited (directly or indirectly) from `a_class`;
        otherwise returns `False`.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
