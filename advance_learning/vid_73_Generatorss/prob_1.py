#ques.1 Basic Generator
"""
Write a generator function called count_up_to(n) that yields numbers from 1 to n.
Example: list(count_up_to(5)) → [1, 2, 3, 4, 5]

def count_up_to(n):
    for i in range(1,n+1):
        yield i

print(list(count_up_to(5)))


Ques.2 Even Numbers Generator
Write a generator even_numbers(limit) that yields only even numbers up to limit.
Example: list(even_numbers(10)) → [2, 4, 6, 8, 10]

def even_numbers(limit):
    for i in range(1,limit+1):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))


Ques.3 Squares Generator
Create a generator squares(n) that yields the squares of numbers from 1 to n.
Example: list(squares(4)) → [1, 4, 9, 16]

def squares(n):
    for i in range(1,n+1):
        yield i**2

print(list(squares(4)))


ques.4 Characters Generator
Write a generator char_by_char(word) that yields one character at a time from the given string.
Example: list(char_by_char("Ashu")) → ['A', 's', 'h', 'u']

def char_by_char(word):
    for char in word:
        yield char

print(list(char_by_char("python")))


ques.5 Multiplication Table Generator
Write a generator table_of(n, limit) that yields multiplication table of n up to limit.
Example: list(table_of(2, 5)) → [2, 4, 6, 8, 10]

def table_of(n, limit):
    for i in range(1, limit+1):
        yield n*i

print(list(table_of(2,5)))
"""

import copy
list1 = [[1,2,3], [4,5,6], [7,8,9]]
list2 = copy.deepcopy(list1)

list2[1][0] = 222

print(list2)
print(list1)
