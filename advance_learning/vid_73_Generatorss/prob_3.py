"""
Ques 1.
Read File in Chunks
Banao ek generator read_in_chunks(file, size) jo file ko given chunk size ke hisaab se yield kare.
👉 Example: agar file hai "HelloWorld" aur size=3 → ["Hel", "loW", "orl", "d"]

solution 1.
import textwrap
def read_in_chunks(file,size):
    chunk = textwrap.wrap(file, size)
    yield from chunk

print(list(read_in_chunks("hellothere",3)))

solution 2.
def read_in_chunks(file, size):
    chunk = [ file[i:i+size] for i in range(0, len(file), size)]
    yield from chunk

print(list(read_in_chunks("helloworld",3)))


Ques 2.
Circular List Generator
Ek generator banao jo ek list ke elements ko circular fashion me infinite tak yield kare.
👉 Example: list(circular([1,2,3], 7)) → [1,2,3,1,2,3,1]

def circular(list1, n):
    i = 0
    while i < n:
        yield list1[i % len(list1)]
        i += 1

print(list(circular([4,5,6], 8)))


Ques 3. Filtered Generator Pipeline
Banao ek pipeline:
Ek generator numbers 1–50 tak yield kare.
Dusra generator sirf unka square kare.
Teesra generator sirf even squares ko yield kare.
Final result: [4, 16, 36, ...]

def number_generator():
    i = 1
    while i <= 50:
        yield i
        i += 1

def number_square(list1):
    for n in list1:
        yield n * n

def even_number(list2):
    for n in list2:
        if n % 2 == 0:
            yield n


result1 = list(number_generator())
result2 = list(number_square(result1))
result3 = list(even_number(result2))
print(result3)


Ques 4. Temperature Alert System
Banao ek generator jo random temperatures generate kare (20–40 range).
Agar temperature 35 se upar ho toh "ALERT" yield kare warna value normal return kare.

import random as rand
def rand_gen():
    while True:
        rand_val = rand.choice(range(20, 41))
        if rand_val >= 35:
            yield "ALERT"
        else:
            yield rand_val   #in the generators return is not meant to produce an output it usually terminate and exits the generator

print(next(rand_gen()))


Ques 5. Reverse Word by Word
Ek generator reverse_words(sentence) banao jo ek sentence ko word-by-word reverse karke yield kare.
👉 Example: "I love Python" → ["I", "evol", "nohtyP"]

def reverse_word(sentence):
    sentence = sentence.split(" ")
    for word in sentence:
        yield word[::-1]

print(list(reverse_word("i love burger pizza")))


Ques 6. Nth Fibonacci Using Generator
Banao ek generator jo fibonacci numbers infinite tak generate kare. Phir usme se sirf Nth number pick karke return karo.
"""
def fibonacci1(n):
    a, b = 0, 1
    list1 = []
    for _ in range(n):
        list1.append(a)
        a, b = b, a + b
    yield list1[len(list1) - 1]

print(list(fibonacci1(10)))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
n = 10
for _ in range(n):
    num = next(gen)
print(num)   # Nth Fibonacci

