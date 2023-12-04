#!/usr/bin/python3
"""Define a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """Class body."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter format.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
