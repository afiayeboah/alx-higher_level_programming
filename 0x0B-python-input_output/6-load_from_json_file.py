#!/usr/bin/python3
"""JSON File Loader Module"""
import json


def load_from_json_file(filename):
    """
    Loads data from a JSON-formatted file and returns the corresponding object.

    :param filename: The name of the file to load JSON data from.
    :type filename: str

    :return: The loaded object from the JSON file.
    :rtype: Any
    """
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file_loaded)
