#!/usr/bin/python3
"""
This module contains a function to read a text file and print its content to stdout.
"""

def read_file(filename=""):
    """
    Reads a UTF8 text file and prints its content to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
