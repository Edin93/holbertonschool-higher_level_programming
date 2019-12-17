#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lent1 = len(tuple_a)
    lent2 = len(tuple_b)
    t1 = 0
    t2 = 0
    if lent1 > 0:
        t1 += tuple_a[0]
        if lent1 == 2:
            t2 += tuple_a[1]
    if lent2 > 0:
        t1 += tuple_b[0]
        if lent2 == 2:
            t2 += tuple_b[1]
    t = t1, t2,
    return t
