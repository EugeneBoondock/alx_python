#!//usr/bin/python3
"""
Empty BaseGeometry Module
"""
class BaseGeometry:
    """
    Raises exceptions and there are values involved
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = str(name)
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
        self.value = value

"""
Inherits from BaseGeometry
"""
class Rectangle(BaseGeometry):
    """
    defines and initializes width and height
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, width, height):
        return super().integer_validator(width, height)
