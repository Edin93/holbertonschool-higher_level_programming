#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = sorted([key for key in a_dictionary.keys()])
    for item in l:
        print(item,': ', a_dictionary[item], sep="")
