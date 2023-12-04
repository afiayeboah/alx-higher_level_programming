#!/usr/bin/python3
"""Define a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Set a new attribute for an object if applicable.
    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute.")
    setattr(obj, att, value)
