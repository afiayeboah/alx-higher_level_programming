#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Representation of a square.

    Attributes:
        _size (int): The size of the square.
        _position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0))
        : Initialize a new Square with a specified size and position.
        size(self): Get the size of the square.
        size(self, value): Set the size of the square.
        position(self): Get the position of the square.
        position(self, value): Set the position of the square.
        calculate_area(self): Calculate and return the area of the square.
        my_print(self): Print the square to stdout with specified character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is
            not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self._position = value

    def calculate_area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square to stdout with the specified character."""
        if self._size == 0:
            print("")
            return

        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0], end="")
            print("#" * self._size)
