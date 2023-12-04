#!/usr/bin/python3
"""Define a class MyList that inherits from the list class."""


class MyList(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Print a sorted version of the list."""
        print(sorted(self))
