#!/usr/bin/python3

"""Define the Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class body."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
