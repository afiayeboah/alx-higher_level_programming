#!/usr/bin/python3
"""Define a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """Class body."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter format."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
