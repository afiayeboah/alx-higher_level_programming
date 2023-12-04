#!/usr/bin/python3
"""Define a function to retrieve available attributes/methods of an object."""


def lookup(obj):
    """Retrieve a list of available attributes."""
    return dir(obj)
