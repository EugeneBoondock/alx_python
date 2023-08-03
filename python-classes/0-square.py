#!/usr/bin/python3
"""

This module Initializes a square instance
with a given size

"""

class Square:
    """
    class named Square
    """
    def __init__(self, size):
        """
        Initialize a Square instance with the given size.

        Parameters:
        size (int): The side length of the square.
        """
        self.__size = size

my_square = Square()