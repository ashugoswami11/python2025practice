"""
Level 1: Very Easy (Baby Steps)

👉 Ye problems sirf recursion + caching ka taste dene ke liye hain.

Factorial using Recursion
Function likho jo factorial nikalta hai n!.
Example: factorial(5) = 120

Factorial using Caching
Same factorial function par @lru_cache lagao. Dekho jab repeat calls karte ho to speed up ho jata hai.

from functools import lru_cache


@lru_cache(maxsize=None)
def facto_func(n):
    if n <2:
        return 1
    else:
        return n * facto_func(n-1)

print(facto_func(900))
print(facto_func(900))



Level 2: Fibonacci (Thoda Advance)

3. Nth Fibonacci Recursion
Recursively nth fibonacci number return karo.
Example: fib(6) = 8
Nth Fibonacci with Caching
Upar wale ko caching ke saath optimize karo.
Print Fibonacci Sequence up to N
Recursively numbers print karna aur caching ka effect dekhna.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibo_func(n):
    if n < 2:
        return 1
    else:
        return fibo_func(n-1) + fibo_func(n-2)

print(fibo_func(150))
print(fibo_func(150))


#-------------------------------------------------------------------------------
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fibo_func(n):
#     recusive function with the caching shows the impressive gain in the speed and change the time complexity from O(2^n) to O(n)
#     if n < 2:
#         return 1
#     else:
#         return fibo_func(n-1) + fibo_func(n-2)
#
# n = int(input("tell me a number which fibonacci sequence you want to print\n"))
#
# for i in range(n):
#     print(fibo_func(i))



Level 3: Simple Grid (Mini Mazes )

 Yahan se hum grid traversal start karenge.
6. Count Paths in 1D
Tumhare paas ek seedhi line me n steps hain. Tum ek step ya do step aage ja sakte ho.
Question: Kitne tarike hain end tak pahuchne ke?
(Ye Fibonacci pattern niklega )

def paths_to_end(n):

    if n == 1 or n == 0:
        return 1
    else:
        return paths_to_end(n - 1) + paths_to_end(n - 2)


print("these much of ways ", paths_to_end(5))


Count Paths in 2D Grid (Only Right & Down)
Ek m x n grid hai. Tum (0,0) se (m-1,n-1) tak ja rahe ho. Sirf right aur down allowed hai.
Question: Total kitne paths hain?
Example: 2x2 grid me → 2 paths.

"""
grid = [[2, 4, 6],
        [1, -1, 9],
        [7, 5, 8]]

rows = len(grid) #it counts inner list as a single element
cols = len(grid[0]) #lenth of inner list are the number of columns

def paths_to_2d_grid(i, j):#we are going to give starting point of matrix to this function which is basically(0, 0)

    if i >= rows or j >= cols:
        return float('inf') # it is a way of writing positive infinity number in python

    if i == rows - 1 and j == cols - 1:
        return grid[i][j]

    if grid[i][j] == -1:
        return float('inf')

    right_ways =  paths_to_2d_grid(i, j+1) # pehle ye infinity right fir infinity down(full execution)
    down_ways  =  paths_to_2d_grid(i+1, j) # fir ye infinity down fir infinity right(full execution)

    return grid[i][j] + min(right_ways, down_ways)

print("minimum path cost: ", paths_to_2d_grid(0, 0))
