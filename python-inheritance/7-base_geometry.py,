#!/usr/bin/python3
"""
Module: base_geometry

This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base class for geometry operations.
    """

    def area(self):
        """
        Raises an exception with a message indicating that
        the method area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (any): The value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
