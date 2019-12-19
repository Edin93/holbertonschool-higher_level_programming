#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_arrs = []
    for k, v in a_dictionary.items():
        if v == value:
            key_arrs.append(k)
    for k in key_arrs:
        del a_dictionary[k]
    return a_dictionary
