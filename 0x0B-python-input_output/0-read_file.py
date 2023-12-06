#!/usr/bin/python3
"""File Reader Module"""


def read_file(filename=""):
    """
    Reads the contents of a text file (UTF-8) and prints the result to stdout.

    :param filename: The name of the file to be read.
    :type filename: str
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
