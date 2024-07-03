#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        side_length (float): The length of each side of the square.

    Methods:
        area(): Computes the area of the square.
        perimeter(): Computes the perimeter of the square.
    """

    def __init__(self, side_length):
        """
        Initializes a square with the given side length.

        Args:
            side_length (float): The length of each side of the square.
        """
        self.side_length = side_length

    def area(self):
        """
        Computes the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Computes the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.side_length
