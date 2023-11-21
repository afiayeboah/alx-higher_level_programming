#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square.

    Attributes:
        _size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square with a specified size.
        size(self): Get the size of the square.
        size(self, value): Set the size of the square.
        area(self): Calculate and return the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size
