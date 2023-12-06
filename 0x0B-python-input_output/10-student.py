#!/usr/bin/python3
"""Student Class Definition"""

class Student:
    """Represents an individual student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize the properties of a student.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert student attributes to a JSON-like dictionary.

        :param attrs: A list of attribute names to include in the dictionary.
        :type attrs: list

        :return: A dictionary containing the specified attributes or all attributes if not provided.
        :rtype: dict
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
