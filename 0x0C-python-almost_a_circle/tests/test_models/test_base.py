#!/usr/bin/python3
"""
Unittest for base class Base
"""
import unittest
Base = __import__('base').Base


class TestBase(unittest.TestCase):
    """
    Test class for Base Class.
    """
    def test_base(self):
        """
        Testing Base class id's value.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(500)
        self.assertEqual(b3.id, 500)
'''
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(500).id, 500)
        self.assertEqual(Base(None).id, 4)
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base(9090).id, 9090)
        self.assertEqual(Base().id, 7)
'''
