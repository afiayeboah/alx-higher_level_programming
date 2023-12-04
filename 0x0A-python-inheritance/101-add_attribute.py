#!/usr/bin/python3
"""Define a function to add attributes to objects."""


def add_attribute(target_object, attribute_name, attribute_value):
    """Set a new attribute for an object if applicable.
    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(target_object, "__dict__"):
        raise TypeError("Can't add new attribute.")
    setattr(target_object, attribute_name, attribute_value)
