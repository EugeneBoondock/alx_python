#!/usr/bin/python3
"""
Empty BaseGeometry Module
"""
class BaseGeometry:
    """
    empty
    """
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.exclude = ['__init_subclass__']

    def __dir__(self):
        return [attr for attr in dir(self) if attr not in self.exclude]
