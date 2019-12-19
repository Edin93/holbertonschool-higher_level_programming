#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = next(iter(a_dictionary))
    max = a_dictionary[best_key]
    for k, v in a_dictionary.items():
        if v > max:
            best_key = k
    return best_key
