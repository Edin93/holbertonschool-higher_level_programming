#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for char in my_string:
        if char != 'C' and char != 'c':
            str += char
    return str
