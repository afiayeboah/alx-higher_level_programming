#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for char str:
        if 'a' <= char <= 'z':
            str += "{:s}".format(chr(ord(char) - 32))
        else:
            str += "{:s}".format(char)
    print(str, end="")
