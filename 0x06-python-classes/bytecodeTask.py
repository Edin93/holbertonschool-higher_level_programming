#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        """
        Init magic class.

        Parameters:
        radius (int, float): the class radius value.
        """
        self._MagicClass__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns: int: area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns: int: circumference."""
        return 2 * math.pi * self._MagicClass__radius
