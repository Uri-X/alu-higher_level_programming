#!/usr/bin/python3

for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        if tens_digit == 8 and units_digit == 9:
            print("89")
        else:
            print("{:d}{:d}".format(tens_digit, units_digit), end=", ")
