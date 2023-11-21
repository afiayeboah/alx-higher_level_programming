#!/usr/bin/python3
"""MagicClass definition for geometric calculations."""
import math


class MagicClass:
    """Representation of a circle for geometric calculations.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (float): The radius of the circle.
        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
