#!/usr/bin/python3
"""
This module defines the Rectangle class, which is a subclass of the Base class.
"""
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
        if new_width > 0:
            self.__width = new_width
        else:
            raise ValueError("Value should be greater than 0")

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
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Value should be greater than 0")

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
        if new_x < 0:
            raise ValueError("Value should be greater than 0")
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
        if new_y < 0:
            raise ValueError("Value should be greater than 0")
        else:
            self.__y = new_y
