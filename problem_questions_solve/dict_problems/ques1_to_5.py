#solution by using Counter from the collections module
"""
from collections import Counter

sales1 = {'apple': 50, 'banana': 20, 'orange': 30}
sales2 = {'banana': 10, 'kiwi': 15, 'apple': 25}

merged = Counter(sales1) + Counter(sales2)

print(type((merged)))

"""

#solution by using for loops

sales1 = {'apple': 50, 'banana': 20, 'orange': 30}
sales2 = {'banana': 10, 'kiwi': 15, 'apple': 25}

sales3 = sales1.copy()
sales3.update(sales2)

for key in sales2:
    if key in sales1:
        sales3[key] = sales1[key] + sales2[key]

print(sales3)
