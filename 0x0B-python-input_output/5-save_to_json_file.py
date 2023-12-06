#!/usr/bin/python3

"""JSON File Saver Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a JSON-serializable object to a text file in JSON format.

    :param my_obj: The object to be saved to the file.
    :type my_obj: Any
    :param filename: The name of the file to which the object is saved.
    :type filename: str
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)
