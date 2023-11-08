#!/usr/bin/python3
def complex_delete(a_dictionary, target_value):
    tmp = a_dictionary.copy()
    for key, value in tmp.items():
        if target_value == value:
            a_dictionary.pop(key)
    return a_dictionary
