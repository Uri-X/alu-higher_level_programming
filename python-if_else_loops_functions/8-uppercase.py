#!/usr/bin/python3


def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()


# Example usage:
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
