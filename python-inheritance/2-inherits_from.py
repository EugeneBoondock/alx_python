#!/usr/bin/python3
"""
This module returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""
def inherits_from(obj, a_class):
    """
    function does what's mentioned above
    """
    if issubclass(type(obj), a_class):
        return True
    elif isinstance(obj, type):
        return True
    else:
        return False
