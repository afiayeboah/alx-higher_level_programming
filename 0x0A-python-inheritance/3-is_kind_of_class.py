#!/usr/bin/python3
"""Define a class and a function to check if an object
is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj to.
    Returns:
        Boolean indicating if obj is an instance or inherited instance.
    """
    return isinstance(obj, a_class)
