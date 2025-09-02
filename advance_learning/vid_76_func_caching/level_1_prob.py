"""
Level 1: Very Easy (Baby Steps)

👉 Ye problems sirf recursion + caching ka taste dene ke liye hain.

Factorial using Recursion
Function likho jo factorial nikalta hai n!.
Example: factorial(5) = 120

Factorial using Caching
Same factorial function par @lru_cache lagao. Dekho jab repeat calls karte ho to speed up ho jata hai.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def facto_func(n):
    if n <2:
        return 1
    else:
        return n * facto_func(n-1)


print(facto_func(900))
print(facto_func(900))


