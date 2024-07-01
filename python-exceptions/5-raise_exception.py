#!/usr/bin/python3
def check_integer(value):
    if not isinstance(value, int):
        raise TypeError("Expected an integer")
    else:
        print(f"The value {value} is an integer")
