#!/usr/bin/python3
"""
This module defines a square by a private instance
instantiation is optional.
"""
class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative integer.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with the given size.

        Parameters:
            size (int, optional): The side length of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size