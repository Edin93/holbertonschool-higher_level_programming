#!/usr/bin/python3
"""
Unittest for base class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for Base Class.
    """
    def test_base(self):
        """
        Testing Base class id's value.
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(500)
        self.assertEqual(b3.id, 500)
        b4 = Base(None)
        self.assertEqual(b4.id, 3)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)
        b6 = Base(9090)
        self.assertEqual(b6.id, 9090)
        b7 = Base()
        self.assertEqual(b7.id, 4)
