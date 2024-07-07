#!/usr/bin/python3
"""
Module for Square class.

This module provides a simple Square class that includes a private instance
attribute for size.
"""

class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
