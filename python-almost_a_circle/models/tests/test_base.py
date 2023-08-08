import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_without_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
