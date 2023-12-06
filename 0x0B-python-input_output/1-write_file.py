#!/usr/bin/python3
"""File Writer Module"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file.

    :param filename: The name of the file to be written.
    :type filename: str
    :param text: The string to be written to the file.
    :type text: str

    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
