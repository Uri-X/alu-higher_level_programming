#!/usr/bin/python3

"""
2-uniq_add.py

Function to add all unique integers in a list (each integer only once).
"""

def uniq_add(my_list=[]):
    """
    Adds all unique integers in `my_list` and returns the sum.

    Args:
        my_list (list): The list from which unique integers will be summed up. Defaults to [] if not provided.

    Returns:
        int: The sum of all unique integers in `my_list`.
    """
    unique_numbers = set()  # Using a set to store unique integers
    
    # Iterate through my_list and add unique integers to unique_numbers set
    for num in my_list:
        unique_numbers.add(num)
    
    # Calculate the sum of unique numbers
    total_sum = sum(unique_numbers)
    
    return total_sum

# Example usage
if __name__ == "__main__":
    # Example list
    my_list = [1, 2, 2, 3, 4, 4, 5]
    # Calculate sum of unique integers
    result = uniq_add(my_list)
    # Print the result
    print("Sum of unique integers in the list:", result)
