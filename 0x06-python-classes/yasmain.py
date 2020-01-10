#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

mc3 = MagicClass(10)
print("mc3 area type: {}".format(type(mc3.area())))
print("{:.2f}".format(mc3.area()))

mc4 = MagicClass(10)
print("mc4 circumference type: {}".format(mc1.circumference()))
print("{:.2f}".format(mc4.circumference()))
