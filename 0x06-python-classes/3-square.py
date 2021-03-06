#!/usr/bin/python3
class Square:
    """Defines a square by size.
    Attributes:
        size (int): square size.
    """

    def __init__(self, size=0):
        """square class constructor.
        Parameters:
            size (int): square size, default value is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the square area.

        Returns:
        int: the current square area.
        """
        return self.__size * self.__size
