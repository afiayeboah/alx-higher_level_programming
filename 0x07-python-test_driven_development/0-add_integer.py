#!/usr/bin/python3

"""
add_integer Module

This module defines the function "add_integer".

Usage:
    result = add_integer(a, b=98)

Raises:
    TypeError: If either 'a' or 'b' is not an integer or float.
"""


def add_integer(a, b=98):
    """Adds two integers or floats."""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
