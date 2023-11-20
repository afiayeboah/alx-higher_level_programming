#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, FloatingPointError) as e:
        div = None
        print("Exception: {}".format(e))
    finally:
        print("Inside result: {}".format(div))
    return div
