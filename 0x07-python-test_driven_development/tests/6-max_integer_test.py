#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer
    """

    def test_empty_list(self):
        """When the list is empty, return None
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_positive_nums_only(self):
        """test positive ints and floats"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([1.45, 1.46, 1.36, 1.455]), 1.46)
        self.assertEqual(max_integer([1]), 1)

    def test_negative_nums(self):
        """test negative ints and floats
        also test the zero boundary
        """
        self.assertEqual(max_integer([-6, -8, -10]), -6)
        self.assertEqual(max_integer([-6, -8, 0]), 0)
        self.assertEqual(max_integer([-6, -8, 0, 10000]), 10000)
        self.assertEqual(max_integer([0.1, 0, -0.1]), 0.1)

    def test_not_all_numbers(self):
        """test if an element is anything other than an int of float
        """
        with self.assertRaises(TypeError):
            max_integer([5, '5', 3])
