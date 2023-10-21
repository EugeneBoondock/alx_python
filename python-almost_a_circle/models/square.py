"""
This module defines the Square class, which is a subclass of the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.

    Attributes:
        width (int): Width of the square.
        height (int): Height of the square.
        x (int): X-coordinate of the top-left corner.
        y (int): Y-coordinate of the top-left corner.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Length of one side of the square.
            x (int, optional): X-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Property for the size of the square (same as width).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): Value to set the size of the square to.
        """
        self.width = value
        self.height = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.width * self.width

    def display(self):
        """
        Prints a visual representation of the square using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
