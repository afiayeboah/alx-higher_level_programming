#!/usr/bin/python3
import sys


def safe_function(func, *args):
    try:
        result = func(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
