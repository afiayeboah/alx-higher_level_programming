#!/usr/bin/python3
"""Define a method for checking inheritance."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.
    Returns:
        Boolean indicating if obj is an inherited instance.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
