#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square with a specified size.
        calculate_area(self): Calculate and return the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def calculate_area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
