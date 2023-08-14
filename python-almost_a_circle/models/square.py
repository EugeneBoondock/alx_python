#!/usr/bin/python3
"""
This module defines the Rectangle class, which is a subclass of the Base class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.

    Attributes:
        __width (int): one size of the square.
        __height (int): second size of the square.
        __x (int): X-coordinate of the top-left corner.
        __y (int): Y-coordinate of the top-left corner.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): one size of the square.
            size (int): second size of the square.
            x (int, optional): X-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints out the sring output
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
    
    @property
    def size(self):
        """
        int: The size of the square (equal width and height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value.

        Raises:
            ValueError: If the size value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError(" width must be greater than 0")

        self.width = value
        self.height = value
