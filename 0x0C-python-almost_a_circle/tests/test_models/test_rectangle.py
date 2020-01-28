#!/usr/bin/python3
"""
Module to test Rectangle Class.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class to test rectangle class.
    """

    def test_none_values(self):
        """
        Test Rectangle class none values for height and width.
        """
        r = Rectangle(30, 14, 0, 0)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 14)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
        r = Rectangle(50, 25, 100, 50)
        self.assertEqual(r.width, 50)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 100)
        self.assertEqual(r.y, 50)
