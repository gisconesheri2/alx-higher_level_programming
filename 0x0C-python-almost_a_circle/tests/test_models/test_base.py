#!/usr/bin/python3
"""test the Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test the creation of the id attribute"""

    def test_id_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_num(self):
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_id_none_2nd_time(self):
        b3 = Base()
        self.assertEqual(b3.id, 2)
