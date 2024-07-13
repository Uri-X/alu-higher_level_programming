#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order

        Example:
        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        """
        print(sorted(self))

# Ensure the file ends with a newline
