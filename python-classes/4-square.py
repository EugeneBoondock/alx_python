#!/usr/bin/python3
"""
This module defines a square by a private instance
instantiation is optional.
Handles the square sizes and the printing 
of # at the end.
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

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Parameters:
            value (int): The new side length value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print the square using the '#' character.

        Example:
        A square with size 3 will be printed as follows:
        ###
        ###
        ###
        
        """
        for _ in range(self.__size):
            print('#' * self.__size)
          if self.__size == 0:
            print('/n')