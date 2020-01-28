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

    def test_normal_values(self):
        """
        Test Rectangle class with normal values.
        """
        r = Rectangle(30, 14, 0, 0)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 14)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertNotEqual(r.id, 149493216)

        r = Rectangle(50, 25, 100, 50)
        self.assertEqual(r.width, 50)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 100)
        self.assertEqual(r.y, 50)

    def test_non_integer_values(self):
        """
        Test Rectangle class with non integer values.
        """
        args = ('10', 20, 10, 2)
        self.assertRaises(TypeError, Rectangle, args)

        args = ((5), 20, 10, 2)
        self.assertRaises(TypeError, Rectangle, args)

        args = ([15], 20, 10, 2)
        self.assertRaises(TypeError, Rectangle, args)

        args = (12, [67], 10, 2)
        self.assertRaises(TypeError, Rectangle, args)

        args = (16, (8), 10, 2)
        self.assertRaises(TypeError, Rectangle, args)

        args = (5, '14', 1, 1)
        self.assertRaises(TypeError, Rectangle, args)

        args = ('15', '30', 0, 50)
        self.assertRaises(TypeError, Rectangle, args)

        args = (20, 40, '60', 10)
        self.assertRaises(TypeError, Rectangle, args)

        args = (40, 20, [15], '5')
        self.assertRaises(TypeError, Rectangle, args)

        args = (15, 45, (17), '15')
        self.assertRaises(TypeError, Rectangle, args)

        args = ([14], 50, '16', 10)
        self.assertRaises(TypeError, Rectangle, args)

    def test_not_valid_values(self):
        """
        Test Rectangle class with non value integer values.
        """
        args = [0, 15, 10, 10]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [20, -20, 100, 20]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [10, 0, 5, 12]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [-10, 82, 5, 12]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [10, 30, -5, 12]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [40, 20, 50, -12]
        self.assertRaises(ValueError, Rectangle, *args)

        args = [60, 30, -100, 0]
        self.assertRaises(ValueError, Rectangle, *args)

    def test_area(self):
        """
        Test rectangle's calculated area.
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        self.assertNotEqual(r1.area(), -6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        self.assertNotEqual(r2.area(), 30)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        self.assertNotEqual(r3.area(), 90)

    def test_update(self):
        """
        Test rectangle's update function.
        """
        r1 = Rectangle(12, 15)
        args = [999, '10', 20, 10, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [999, (5), 20, 10, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [999, [15], 20, 10, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [888, 12, [67], 10, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [888, 16, (8), 10, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [888, 5, '14', 1, 1]
        self.assertRaises(TypeError, r1.update(args))

        args = [888, '15', '30', 0, 50]
        self.assertRaises(TypeError, r1.update(args))

        args = [999, 20, 40, '60', 10]
        self.assertRaises(TypeError, r1.update(args))

        args = [999, 40, 20, [15], '5']
        self.assertRaises(TypeError, r1.update(args))

        args = [999, 15, 45, (17), '15']
        self.assertRaises(TypeError, r1.update(args))

        args = [999, [14], 50, '16', 10]
        self.assertRaises(TypeError,  r1.update(args))

        args = [999, 0, 15, 10, 10]
        self.assertRaises(ValueError,  r1.update(args))

        args = [999, 20, -20, 100, 20]
        self.assertRaises(ValueError,  r1.update(args))

        args = [999, 10, 0, 5, 12]
        self.assertRaises(ValueError,  r1.update(args))

        args = [888, -10, 82, 5, 12]
        self.assertRaises(ValueError,  r1.update(args))

        args = [888, 10, 30, -5, 12]
        self.assertRaises(ValueError, r1.update(args))

        args = [888, 40, 20, 50, -12]
        self.assertRaises(ValueError, r1.update(args))

        args = [888, 60, 30, -100, 0]
        self.assertRaises(ValueError, r1.update(args))

        r1 = Rectangle(10, 50, 15, 25)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 50)
        self.assertEqual(r1.x, 15)
        self.assertEqual(r1.y, 25)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update(70)
        self.assertEqual(r1.id, 70)
        r1.update(80, 666)
        self.assertEqual(r1.id, 80)
        self.assertEqual(r1.width, 666)
