#in python there are iterable, iterators, iteration
"""
1. iterable:-- it is a python object a collection whose values can be access one by one
2. iterators:-- they are used to fetch iterable values
3. iteration:-- it is a process of in which iterable values are fetch with the help of iterators
"""

list = ["ashu", 's', 899, True]

try:
    li_elements = iter(list)
except TypeError:
    print("out of range error of iteration")

print(next(li_elements))
print(next(li_elements))
print(next(li_elements))
print(next(li_elements))
print(next(li_elements))
