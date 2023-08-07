#!/usr/bin/python3
"""
This module checks if an object is an instance of a class using isinstance
"""
def is_same_class(obj, a_class):
    """
    This function defines an object and a class
    """
    if isinstance(obj, a_class):
        return isinstance(obj, a_class)
    else:
        return False
