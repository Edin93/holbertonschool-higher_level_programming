#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = sorted([key for key in a_dictionary.keys()])
    for item in list:
        print(item, ': ', a_dictionary[item], sep="")
