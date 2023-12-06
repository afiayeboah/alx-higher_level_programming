#!/usr/bin/python3
"""File Appender Module"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file.

    :param filename: The name of the file to which the string is appended.
    :type filename: str
    :param text: The string to be appended to the file.
    :type text: str

    :return: The number of characters appended to the file.
    :rtype: int
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
