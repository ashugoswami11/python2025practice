"""
prob 1:---

text = "apple banana apple orange banana apple"

text = text.split() #split converts a string into list of sub-strings

new_dict = {}
for i in text:
    if i not in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1

print(new_dict)

"""
#prob 2:--
"""
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 15, 'd': 25}

dict3 = {}
dict3 = dict1.copy()

for key, value in dict2.items():
    if key in dict3:
        dict3[key] += value
    else:
        dict3[key] = value
print(dict3)
"""

#prob 3:--
"""
students = {
    '101': {'name': 'Ashu', 'marks': 85},
    '102': {'name': 'Ravi', 'marks': 78}
}

for i in students:
    if students[i]['name'] == 'Ravi':
        students[i]['marks'] = 90

print(students)

"""
#prob 4:--

employees = [
    {'name': 'Alice', 'dept': 'IT'},
    {'name': 'Bob', 'dept': 'HR'},
    {'name': 'Charlie', 'dept': 'IT'},
    {'name': 'David', 'dept': 'Finance'},
    {'name': 'Eve', 'dept': 'HR'}
]

depart_dict = {}
for i in employees:
    if i['dept'] not in depart_dict:
        depart_dict[i['dept']] = [i['name']]
    else:
        depart_dict[i['dept']].append(i['name'])

print(depart_dict)