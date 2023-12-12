#!/usr/bin/python3
"""Unit tests for the Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unit tests for the Base model"""

    def test_initialization_incremental_ids(self):
        """Test that IDs are incremented correctly during initialization"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_initialization_with_custom_id(self):
        """Test initialization with a custom ID"""
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_with_none_and_empty_list(self):
        """Test to_json_string with None and an empty list"""
        base = Base(1)
        self.assertEqual(base.to_json_string(None), "[]")
        self.assertEqual(base.to_json_string([]), "[]")

    def test_to_json_string_with_valid_list(self):
        """Test to_json_string with a valid list of dictionaries"""
        base = Base(1)
        input_list = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
        expected_output = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
        self.assertEqual(base.to_json_string(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
