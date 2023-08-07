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
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")
        
        self.value = value
