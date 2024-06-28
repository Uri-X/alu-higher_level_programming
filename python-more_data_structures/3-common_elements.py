#!/usr/bin/python3

"""
3-common_elements.py

Function to find and return a set of common elements between two sets.
"""

def common_elements(set_1, set_2):
    """
    Finds and returns a set of common elements between `set_1` and `set_2`.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing common elements between `set_1` and `set_2`.
    """
    return set_1 & set_2

# Example usage
if __name__ == "__main__":
    # Example sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    # Find common elements
    common = common_elements(set1, set2)
    # Print the result
    print("Common elements:", common)
