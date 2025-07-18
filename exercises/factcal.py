# def fact_iterative(n):
#     result = 1
#     for i in range(n):
#         result = result * (i+1)
#     return result
#
# def fact_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n* fact_recursive(n-1)
#
# x = int(input("enter a number\n"))
# # n = fact_iterative(x)
# m = fact_recursive(x)
# print(m)


#########################


# def fibo_func(n):
#     if n < 2:
#         return n
#     else:
#         return fibo_func(n-1) + fibo_func(n-2)

# x = int(input("enter a number\n"))
# for i in range(x):
#     print(fibo_func(i),i)


def fibo_iterative(n):
    b = 0
    c = 1
    if n < 2:
        print(n)
    else:
        for i in range(1,n):
            a = b
            b = c
            c = a + b
        return c

x = int(input("enter a number\n"))
c = fibo_iterative(x)
print(c)