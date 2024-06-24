#!/usr/bin/python3

for tens_digit in range(10):  # tens_digit ranges from 0 to 9
    for units_digit in range(tens_digit + 1, 10):  # units_digit ranges from tens_digit + 1 to 9
        if tens_digit == 8 and units_digit == 9:
            print("89")
        else:
            print("{:d}{:d}".format(tens_digit, units_digit), end=", ")
