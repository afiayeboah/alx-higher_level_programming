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

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        '''Returns string representation of square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
