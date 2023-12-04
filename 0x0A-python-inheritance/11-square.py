#!/usr/bin/python3

"""Define the Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class body."""

    def __init__(self, size):
        """Initialize a Square instance with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
