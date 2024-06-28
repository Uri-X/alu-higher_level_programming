#!/usr/bin/python3

"""
1-search_replace.py

Replace all occurrences of an element by another in a new list.
"""

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of `search` in `my_list` with `replace`.

    Args:
        my_list (list): The initial list where replacements will be made.
        search: The element to search for and replace.
        replace: The new element to replace `search` with.

    Returns:
        list: A new list where all occurrences of `search` in `my_list` are replaced by `replace`.
    """
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

# Example usage
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 3, 4, 2, 5, 2]
    # Replace all occurrences of 2 with 7
    new_list = search_replace(my_list, 2, 7)
    # Print the original and modified lists
    print("Original List:", my_list)
    print("Modified List:", new_list)