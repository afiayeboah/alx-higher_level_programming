#!/usr/bin/python3
"""Student Class Definition"""


class Student:
    """Represents a student with basic information."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student with the provided details.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert the student's attributes to a JSON-like dictionary.

        :return: A dictionary containing the student's attributes.
        :rtype: dict
        """
        return self.__dict__
