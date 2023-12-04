"""
text_indentation Module

This module defines a text-indentation function 'text_indentation(text)'.

Parameters:
    text (str): The text to print.

Raises:
    TypeError: If text is not a string.
"""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""


    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0

    while c < len(text) and text[c] == ' ':
        c += 1


    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
