#!/usr/bin/python3


def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')


# Test cases
if __name__ == "__main__":
    print(islower('a'))  # True
    print(islower('z'))  # True
    print(islower('A'))  # False
    print(islower('Z'))  # False
    print(islower('!'))  # False
    print(islower('m'))  # True
    print(islower('M'))  # False
