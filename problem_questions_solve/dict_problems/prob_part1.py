# task: Count how many times each fruit appears using a dictionary.

"""
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

dict1 = {}
for i in fruits:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)
"""

# 2nd prob:------------

"""
# Task:
# Create a dictionary that counts how many times each name appears.

names = ['Ashu', 'Ravi', 'Ashu', 'Mona', 'Ravi', 'Ravi']

name_dict= {}
for i in names:
    if i in name_dict:
        name_dict[i] += 1
    else:
        name_dict[i] = 1

print(name_dict)
"""

#3rd prob:----------

# Task:
# Reverse this dictionary so names become keys, and their student IDs are stored in a list.
# Output should be:
# {'Ashu': ['101', '103'], 'Ravi': ['102']}

students = {'101': 'Ashu', '102': 'Ravi', '103': 'Ashu'}

reverse_dict = {}
for key, value in students.items():
    if value in reverse_dict:
        reverse_dict[value].append(key)
    else:
        reverse_dict[value] = [key] #important line here key as a list is storing

print(reverse_dict)
