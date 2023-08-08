#!/usr/bin/python3
"""
A module for class Base
"""


import unittest

class Base:
    """
    The base class for managing id attribute in all other classes.

    Attributes:
    __nb_objects (int): Private class attribute to track objects.

    Methods:
        __init__(self, id=None): Class constructor to initialize an instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int, optional): If provided, assigns the id attribute with this value.
            If not provided, increments __nb_objects and assigns the new value to id.
        """
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
"""
Module for class Test
"""


class TestBase(unittest.TestCase):
    """
    Unit tests for the Base class.
    """

    def test_create_instance_with_id(self):
        """
        Test creating an instance of Base with a specific id.
        """
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_without_id(self):
        """
        Test creating an instance of Base without specifying an id.
        """
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
