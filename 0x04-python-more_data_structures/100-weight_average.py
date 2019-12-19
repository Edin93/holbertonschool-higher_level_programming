#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    r = div = 0
    if length == 0:
        return 0
    for item in my_list:
        div += item[1]
        r += item[0] * item[1]
    return r / div
