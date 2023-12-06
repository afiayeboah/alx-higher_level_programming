#!/usr/bin/python3
"""JSON Stringifier Module"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    :param my_obj: The object to be converted to a JSON-formatted string.
    :type my_obj: Any

    :return: The JSON representation of the input object as a string.
    :rtype: str
    """
    return json.dumps(my_obj)
