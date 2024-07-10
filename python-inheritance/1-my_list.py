#!/usr/bin/python3
"""
Module: 1-my_list

The MyList class has method to print the list in ascending order.
"""


class MyList(list):
    """
    MyList class inherits from list and provides additional functionality.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        This method sorts the list and prints it.
        """
        if issubclass(MyList, list):
            print(sorted(self))
