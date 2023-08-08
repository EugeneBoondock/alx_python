#!/usr/bin/python3
import unittest
"""
This is a new module
"""


class Base:
    """
    This class is the base of all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
"""
A unittest class
"""


class TestBase(unittest.TestCase):
    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_without_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
