#!/usr/bin/python3
"""
a function to read a text file and print its content.
"""


def read_file(filename=""):
    """
    Reads (UTF8) and prints it to stdout.

    Args:
        filename (str): name of file. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
    else:
        print("Usage: ./read_file.py <filename>")
