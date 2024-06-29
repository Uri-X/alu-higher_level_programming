#!/usr/bin/python3
# This line indicates that the script should be run using the Python 3 interpreter.

def uniq_add(my_list=[]):
    # Define a function named uniq_add that takes a list (my_list) as an argument.
    # If no argument is provided, it defaults to an empty list.
    
    # Convert the list to a set to remove duplicate values and then sum the unique values.
    return sum(set(my_list))
