#!/usr/bin/python3
"""Unit tests for the Square class
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unit tests for Square model initialization"""

    def test_initialization_success(self):
        """Test successful initialization of Square instances"""
        square1 = Square(5)
        square2 = Square(10)
        self.assertEqual(square1.id, 5)
        self.assertEqual(square2.id, 6)

    def test_initialization_without_arguments(self):
        """Test that initializing Square without arguments raises TypeError"""
        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
