#!/usr/bin/python3

"""JSON String Parser Module"""
import json


def from_json_string(my_str):
    """
    Parses a JSON-formatted string and returns the corresponding object.

    :param my_str: The JSON-formatted string to be parsed.
    :type my_str: str

    :return: The parsed JSON object.
    :rtype: Any
    """
    return json.loads(my_str)
