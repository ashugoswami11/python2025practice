#solution by using Counter from the collections module

"""
Question 1:------

sales1 = {'apple': 50, 'banana': 20, 'orange': 30}
sales2 = {'banana': 10, 'kiwi': 15, 'apple': 25}

sales3 = sales1.copy()

sales3.update(sales2)
# print(sales3)

for keys in sales2:
    if keys in sales1:
        sales3[keys] = sales1[keys]+sales2[keys]


my_sorted = sorted(sales3.items(), key=lambda x: x[1], reverse = True)
print(dict(my_sorted))

"""
from itertools import count

#Question 2:-------
"""
import string

text = "Python is great. Python is dynamic. Python is easy to learn."

new_text = [i for i in text if i not in string.punctuation] #here it is a string iteration and returning a list
new_text = ''.join(new_text) #here list becomes string
new_text = new_text.split()

my_dict = {}
count = 0

for i in new_text:
    if i not in my_dict:
        my_dict.update({i:new_text.count(i)}) # list_name.count("word")

print(my_dict)
"""

#question 3 :-------
"""
students = {'101': 'Ashu', '102': 'Ravi', '103': 'Ashu'}

reverse_dict = {}

for id,name in students.items(): #give tuple(id=101, name="ashu")
    if name in reverse_dict:
        reverse_dict[name].append(id)
    else:
        reverse_dict[name] = [id]

print(reverse_dict)

"""
#question 4:---

employees = {
    'e1': {'name': 'Ashu', 'salary': 45000},
    'e2': {'name': 'Ravi', 'salary': 52000},
    'e3': {'name': 'Mona', 'salary': 49000},
}


highest = dict(sorted(employees.items(),key = lambda x: x[1]["salary"], reverse=True))

print(highest)
