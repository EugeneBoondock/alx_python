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
        int: The width of the rectangle.
        """
        return self.size
    
    @size.setter
    def size(self, width, length, size):
        """
        Set the size of the square.

        Args:
            width (int): The width value.

        Raises:
            ValueError: If the width value is not greater than 0.
        """
        if not isinstance(width, length, int):
            raise TypeError(f"width must be an integer")

        if width > 0:
            self.size = size
        else:
            raise ValueError(f"width must be > 0")
        
        self.width = length
