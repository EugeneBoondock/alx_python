#!/usr/bin/python3
"""
This module is for a Rectangle
"""


from base import Base

class Rectangle(Base):
    """
    Function initialises width, height, x and y
    also the id makes sure everything is int from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            raise ValueError("Value should be greater than 0")

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Value should be greater than 0")

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        if new_x < 0:
            raise ValueError("Value should be greater than 0")
        else:
            print(self.__x)
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if new_y < 0:
            raise ValueError("Value should be greater than 0")
        else:
            print(self.__y)
