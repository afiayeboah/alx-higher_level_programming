#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square.

    Attributes:
        __size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get or set the length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of a side of the square.

        Args:
            value (int): The new length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Size must be an integer')
        if value < 0:
            raise ValueError('Size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __le__(self, other):
        """Check if the area of self is less than or equal
        to the area of another square."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Check if the area of self is less than the
        area of another square."""
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        """Check if the area of self is not equal to
        the area of another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of self is greater than
        the area of another square."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Check if the area of self is equal to the area of another square."""
        return self.area() == other.area()
