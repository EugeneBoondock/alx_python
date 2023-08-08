#!/usr/bin/python3
"""
This module is a Base module
"""


class Base:
    """
    This function increments and assigns stuff
    """
    def __init__(self, id=None):

        __nb_objects = 0

        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
