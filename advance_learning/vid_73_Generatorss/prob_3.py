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


result = even_number(number_square(number_generator()))
print(list(result))

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

gen = rand_gen()
for _ in range(10):
    print(next(gen))


Ques 5. Reverse Word by Word
Ek generator reverse_words(sentence) banao jo ek sentence ko word-by-word reverse karke yield kare.
Example: "I love Python" → ["I", "evol", "nohtyP"]

def reverse_word(sentence):
    sentence = sentence.split(" ")
    for word in sentence:
        yield word[::-1]

print(list(reverse_word("i love burger pizza")))


Ques 6. Nth Fibonacci Using Generator
Banao ek generator jo fibonacci numbers infinite tak generate kare. Phir usme se sirf Nth number pick karke return karo.

def fibo_generator():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b

gen = fibo_generator()
num = 8
for _ in range(num):
    nth = next(gen)

print(nth)


Ques 7. Ek generator banao jo file read kare aur
sirf un lines ko yield kare jisme "ERROR" word ho.

def file_generator(file_name):
    with open(f"{file_name}", "r" ) as f:
        f.readline()
        for line in f:
            have_error = False
            for word in line.split():
                if word == "[ERROR]":
                    have_error = True
                    break
            if have_error :
                yield line


result = list(file_generator("temp.txt"))
for i in result:
    print(">>>",i)



Ques 8. Chunked Prime Stream
Ek generator banao jo prime numbers generate kare aur unhe chunks me yield kare.
Example: prime_chunks(10, 3) → [[2, 3, 5], [7, 11, 13], [17, 19, 23], ...]

def prime_chunks(n, chunk_size):
    x = 0 # increment till x<num
    i = 2 # starting position of prime number
    list1 = []
    while x < n: #  x ki value tab hee increment karna jab koi prime number mil jaaye
        flag = True
        for j in range(2, int(i**0.5)+1): #here if don't add 1 then for e.g 2**0.5 = 1.41 after int(2**0.5) it becomes 1 and in range(start,end) start to end-1 so if i add 2 it will run till 1
            if i % j == 0:
                flag = False
                break
        if flag:
            list1.append(i)
            x += 1 # yaha x ki value tab hee increment hogi jab humko ek prime number mil jayega
        i +=1

    result_list = [list1[k: k+chunk_size]for k in range(0, len(list1), chunk_size)]
    yield from result_list


gen = prime_chunks(10,3)
print(list(gen))
"""
