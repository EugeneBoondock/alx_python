#!/usr/bin/python3
"""
This module defines the Rectangle class, which is a subclass of the Base class.
"""
import unittest
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle, inheriting from the Base class.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the top-left corner.
        __y (int): Y-coordinate of the top-left corner.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def __str__(self):
        """
        Prints out the sring output
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
    
    def update(self, *args, **kwargs):
        """
        Updates the attributes based on the number of arguments
        """
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
        elif not args and kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
    
    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, new_width):
        """
        Set the width of the rectangle.

        Args:
            new_width (int): The new width value.

        Raises:
            ValueError: If the new width value is not greater than 0.
        """
        if not isinstance(new_width, int):
            raise TypeError(f"width must be an integer")

        if new_width > 0:
            self.__width = new_width
        else:
            raise ValueError(f"width must be > 0")

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, new_height):
        """
        Set the height of the rectangle.

        Args:
            new_height (int): The new height value.

        Raises:
            ValueError: If the new height value is not greater than 0.
        """
        if not isinstance(new_height, int):
            raise TypeError(f"height must be an integer")

        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError(f"height must be > 0")

    @property
    def x(self):
        """
        int: The x-coordinate of the top-left corner.
        """
        return self.__x
    
    @x.setter
    def x(self, new_x):
        """
        Set the x-coordinate of the top-left corner.

        Args:
            new_x (int): The new x-coordinate value.

        Raises:
            ValueError: If the new x-coordinate value is less than 0.
        """
        if not isinstance(new_x, int):
            raise TypeError(f"x must be an integer")

        if new_x < 0:
            raise ValueError(f"x must be >= 0")
        else:
            self.__x = new_x
    
    @property
    def y(self):
        """
        int: The y-coordinate of the top-left corner.
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """
        Set the y-coordinate of the top-left corner.

        Args:
            new_y (int): The new y-coordinate value.

        Raises:
            ValueError: If the new y-coordinate value is less than 0.
        """

        if not isinstance(new_y, int):
            raise TypeError(f"y must be an integer")
        
        if new_y < 0:
            raise ValueError(f"y must be >= 0")
        else:
            self.__y = new_y

    def area(self):
        """
        Area for rectangle class blah blah blah
        """
        return self.__width * self.__height

    def display(self):
        """
        hashtag area 
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

"""
Unittest Module
"""
class TestRect(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """

    def test_values_are_integers(self):
        """
        Test checking if values are int.
        """
        y = Rectangle('10', 5, 2, 4)
        self.assertIsInstance(y.id, int)
        self.assertIsInstance(y.width, int)
        self.assertIsInstance(y.height, int)
        self.assertIsInstance(y.x, int)
        self.assertIsInstance(y.y, int)

    def test_values_are_not_integers(self):
        """
        Test checking if values are not int.
        """
        with self.assertRaises(TypeError):
            n = Rectangle('x', 'b', 'q', 'f')

    def test_values_are_greater_than0(self):
        """
        Test checking if values are greater than 0.
        """
        g = Rectangle(1, 4, 6, 4)
        self.assertGreater(g.id, 0)
        self.assertGreater(g.width, 0)
        self.assertGreater(g.height, 0)
        self.assertGreater(g.x, 0)
        self.assertGreater(g.y, 0)

    def test_values_are_less_than0(self):
        """
        Test checking if values are less than 0.
        """
        l = Rectangle(-1, -6, -16, -7)
        self.assertLess(l.id, 0)
        self.assertLess(l.width, 0)
        self.assertLess(l.height, 0)
        self.assertLess(l.x, 0)
        self.assertLess(l.y, 0)

if __name__ == "__main__":
    unittest.main()

