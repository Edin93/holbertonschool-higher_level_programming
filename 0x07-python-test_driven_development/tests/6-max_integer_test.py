#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_function(self):
        self.assertEqual(max_integer([0, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -15, -4]), -1)
        self.assertEqual(max_integer([134, 666, -1000, 67]), 666)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([]), None)
