#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a string after the first occurrence of a specified string in a file.

    :param filename: The name of the file.
    :type filename: str
    :param search_string: The string to search for in each line.
    :type search_string: str
    :param new_string: The string to append after the found search string.
    :type new_string: str
    """
    modified_text = ""
    with open(filename) as read_file:
        for line in read_file:
            modified_text += line
            if search_string in line:
                modified_text += new_string
    with open(filename, "w") as write_file:
        write_file.write(modified_text)
