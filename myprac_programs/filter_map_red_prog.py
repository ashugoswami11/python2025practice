#agenda:-- to create a salary processing system which apply tools filter,maps,reduce
"""
tasks:-
1. we are given a list of employees details along with their salaries
2. filter out employees whose salaries is greater than or equal to 20000 (eligible for bonus)
3. use map function to apply 10% bonus on those salaries and store them into a different list
4, then reduce the list to find out the total amount to be paid after bonuses

******** to apply 10% of that item, On that item we multiply that item with 1.10*******
"""
from functools import reduce

employees = [
    {"name": "Ashu", "salary": 15000},
    {"name": "Riya", "salary": 28000},
    {"name": "Ankit", "salary": 40000},
    {"name": "Alex", "salary": 22000},
    {"name": "Nitin", "salary": 18000}
]

filtered_employees = list(filter(lambda x: x['salary']>=20000,employees))
# print(filtered_employees)

#here we can use the round function to make the  float number precision after the decimal
bonus_applied = list(map(lambda x: round(x['salary']*1.10,2),filtered_employees))  #round func is used
# print(bonus_applied)

amount_after_bonus = reduce(lambda total,salary: total+salary, bonus_applied)
# print(amount_after_bonus)

if len(filtered_employees) == 0:
    print("no one's qualified for the bonus")
else:
    qualified_names = map(lambda x : x["name"],filtered_employees)
    print("employees who are qualified for the bonus: \n" , ' , '.join(qualified_names))

    print("\nsalaries after bonus: \n", bonus_applied)
    print("\ntotal amount to be paid after bonus: \n", amount_after_bonus)

