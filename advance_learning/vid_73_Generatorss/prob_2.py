#ques.1 . Infinite Counter
"""
Banao ek generator infinite_counter(start) jo given number se counting start kare aur infinite tak jaata rahe.

def infinite_counter(start):
    while True:
        yield start
        start += 1

gen = infinite_counter(10)
print(next(gen))
print(next(gen))
print(next(gen))

ques.2 Fibonacci Generator
Banao ek generator fibonacci(n) jo first n Fibonacci numbers generate kare.
Example:
list(fibonacci(7)) → [0, 1, 1, 2, 3, 5, 8]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n): # '_' underscore is a convention here when we don't want the value which used in the iteration we used this underscore convention
        yield a
        a, b = b , a + b

print(list(fibonacci(7)))


ques.3 Prime Numbers Generator
Banao ek generator generate_primes(limit) jo given limit tak ke prime numbers yield kare.
Example:
list(generate_primes(20)) → [2, 3, 5, 7, 11, 13, 17, 19]

def generate_primes(limit):
    for i in range(2,limit+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i

print(list(generate_primes(20)))


Q4. Odd Numbers with Step
Banao ek generator odd_numbers(n, step) jo odd numbers generate kare with a given step.
Example:
list(odd_numbers(10, 2)) → [1, 3, 5, 7, 9]

def odd_numbers(n, step):
    for i in range(1, n+1, step):
        if i % 2 != 0:
            yield i

print(list(odd_numbers(20, 3)))


Q5. Reverse String Generator
Banao ek generator reverse_string(word) jo string ko character by character reverse karke yield kare.
Example:
list(reverse_string("Ashu")) → ['u', 'h', 's', 'A']

def reverse_string(word):
    for i in reversed(word):
        yield i

print(list(reverse_string("ashu")))
"""

