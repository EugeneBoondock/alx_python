#!/usr/bin/python3
"""
Empty BaseGeometry Module
"""
class BaseGeometry:
    """
    empty
    """
    def __dir__(self):
        return [attr for attr in dir(self) if attr != '__init_subclass__']
