# num1 = 32
# num2 = 64
#
# num3 = int(input())
#
# if num3>num1:
#     print("greater")
# else:
#     print("lesser")

# list=[3,4,5]             #in and not in  is also a keyword works as simple english
# if 4 in list:
#     print("yes it is in the list")
# if 24 not in list:
#         print("not in the list")
#
# print(15 in list)

# print("tell me your age")
# age = int(input())
#
# if 100 > age >18 :   #chaining of age  instead of using and keyword
#     print("you can drive")
# elif 1 < age < 18:
#     print("you can't drive")
# elif age==18:
#     print("we can't decide")
# else:
#     print("wrong input")

"""faulty calculator"""


print("please enter num1")
num1 = int(input())

print("please enter num2")
num2 = int(input())

print("please choose the arithmetic operator among '-', '+', '*', '/' ")

op = input()
if op == '+':
    if num1 == 56 and num2 == 29:
        print(77)
    else:
        print(num1 + num2)

elif op == '*':
    if num1 == 43  and num2 == 3:
        print(555)
    else:
        print(num1 * num2)

elif op == '/':
    if num1 == 56  and num2 == 6:
        print(4)
    else:
        print(num1 / num2)

else:
    if op == '-':
        print(num1 - num2)