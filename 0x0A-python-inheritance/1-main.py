#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

print('-'*30)

ml = MyList()
ml.append(14)
ml.append(-13)
ml.append(-100)
ml.append(800)
ml.append(400)
print(ml)
ml.print_sorted()
