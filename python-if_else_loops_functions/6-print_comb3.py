#!/usr/bin/python3

for tens_digit in range(9):  # tens_digit ranges from 0 to 8
    for units_digit in range(tens_digit + 1, 10):  # units_digit ranges from tens_digit + 1 to 9
        if tens_digit != units_digit:
            if tens_digit == 0 and units_digit == 1:
                print("01", end=", ")
            else:
                print("{:d}{:d}".format(tens_digit, units_digit), end=", ")

print("89")
