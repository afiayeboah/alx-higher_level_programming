"""
max_integer Module

Module defines a function 'max_integer(list=[]):

Parameters:
    list (list, optional): A list of integers. Defaults to an empty list.

Returns:
    int or None: The maximum integer in the list. Returns None if the list is empty.
"""

def max_integer(list=[]):
    """Find and return the max integer in a list of integers.
    
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    
    result = list[0]
    i = 1

    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    return result
