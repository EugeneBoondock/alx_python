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

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = int(id)
