#!/usr/bin/python3
"""
This module provides a function to retrieve the list of available attributes
and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to retrieve attributes and methods from.

    Returns:
        list: A list of available attributes and methods.
    """
    return dir(obj)
