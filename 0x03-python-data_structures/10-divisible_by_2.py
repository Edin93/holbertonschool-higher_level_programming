#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = []
    for i in my_list:
        if (i % 2 == 0):
            l.append(True)
        else:
            l.append(False)
    return l
