#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Representation of a square.

    Attributes:
        _size (int): The size of the square.

    Methods:
        __init__(self, size): Initialize a new Square with a specified size.
        size(self): Get the size of the square.
        size(self, value): Set the size of the square.
        calculate_area(self): Calculate and return the area of the square.
        my_print(self): Print the square to stdout using the '#' character.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

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

    def calculate_area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square to stdout using the '#' character."""
        for _ in range(self._size):
            print("#" * self._size)
        if self._size == 0:
            print("")
