#!/usr/bin/python3
"""Module: MyClass - a simple class demonstration."""

class MyClass:
    """A class representing a basic example."""

    def __init__(self, name):
        """
        Initialize a MyClass instance with a given name.
        
        :param name: A string representing the name of the instance.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """
        Return a string representation of the MyClass instance.

        :return: A formatted string containing the instance's name and number.
        :rtype: str
        """
        return f"[MyClass] {self.name} - {self.number}"
