# agenda 1st:-- factorial printing

#### iteratively

# def fact_iterative(n):
#     if n ==0 or n==1:
#         return 1
#     else:
#         result = 1
#         for i in range(1,n+1):
#             result = result * i
#
#     return result

#### recursively

# def fact_recursive(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact_recursive(n-1)


# agenda 2nd:-- fibonacci printing
### iteratively

# def fib_iterative(n,choice):
#     a = 0 #first no. of series
#     b = 1 #second no. of series
#     c = 0
#     if n == 1 or n==0:
#         print(n)
#     if choice == 1 and n >= 2:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             c = a + b
#             print(c)
#             a = b
#             b = c
#     else:
#         for i in range(1,n):
#             a = b
#             b = c
#             c = a + b
#         print(c)
#
#
# print("to print series of fibonacci numbers enter 1\n",
#       "to print the nth fibonacci number enter 2",)
# choice = int(input())
# print("enter a number for fib ")
# u_num = int(input())
# if(u_num < 0):
#     print("enter a positive number")
# else:
#     fib_iterative(u_num,choice)


###fib recursive
def fibo_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


print("to print series of fibonacci numbers enter 1\n",
        "to print the nth fibonacci number enter 2",)
choice = int(input())
print("enter a number for fib ")
u_num = int(input())
if choice == 2:
    print(fibo_recursive(u_num-1))
else:
    for i in range(0,u_num):
        print(fibo_recursive(i))

