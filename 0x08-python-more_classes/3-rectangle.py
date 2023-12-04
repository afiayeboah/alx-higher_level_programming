#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Class representing a rectangle. """

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with specified width and height.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns a string representation of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be non-negative.")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be non-negative.")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of a Rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
