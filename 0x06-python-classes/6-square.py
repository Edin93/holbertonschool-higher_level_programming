#!/usr/bin/python3
class Square:
    """Defines a square by size.
    Attributes:
        size (int): square size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """square class constructor.
        Parameters:
        size (int): square size, default value is 0.
        position (tuple): x and y positions.
        """
        self.size = size
        self.position = position


    @property
    def size(self):
        """Retrieve size from class.
        Returns:
        int: the square size.
        """
        return self.__size


    @size.setter
    def size(self, value):
        """square size setter.
        Parameters:
        value (int): square size.

        Returns:
        int: square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    @property
    def position(self):
        """Retrieve square position.

        Return:
        tuple: square position.
        """
        return self.__position


    @position.setter
    def position(self, value):
        """Set square position.

        Parameters:
        value (tuple): position tuple value.

        Returns:
        tuple: square's position.
        """
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the square area.
        Returns:
        int: the current square area.
        """
        return self.__size * self.__size


    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] <= 0:
                    for x in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
