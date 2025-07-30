# groccery = ["books", "lemon", "harpic", "salt"]
# print(type(groccery))
#
# numlist = [34,34,5,6,76,66,34]
# # numlist.sort() #it works outside the print statement
# numlist.pop()
# print(numlist)
#
# print(groccery[0][0:3])
# print(max(groccery)) #for the list of string items max and min give the result in the form of the index number not in the biggest or smallest
# groccery.append("soybean")  #it also works outside the print statement
# print(groccery)
#
# #tuples are initiated with the parenthesis
# #list can contains many methods whereas tuples have fewer
# tup= (45,34,23,"haary")
# tup1=("miss", "oxford", "mit")
#
# print(tup)
# print(tup1.count("oxford"))
# print(tup1.index("mit"))
# tup2= (1,)  #to make the tuple of one item we have to put a comma after the value so that compiler understand it as a tuple not a value inside   parenthesis
#
# # swapping 2 numbers
# a=9
# b=7
# a,b = b,a
# print(a,b)
# groccery.extend(numlist)
# print(groccery)

# tup1 = (23,5,633,23,87,4,9,97,60,44,59,96,25,64)
#
# # print(tup1.__sizeof__()) #use of __sizeof__() function

# ###########list comprehension------------------------------


# ls = [i for i in tup1 if i %2 !=0]
# print(ls)
# print(type(ls))

#multiply corresponding items of the lists
# list1 = [26,5,633,23,87,4,9,97,60,44,59,96,25,64]
# list2 = [2,57,63,33,7,56,998,78,6,4,590,6,52,649]


# list3 = [(i*j) for i,j in zip(list1,list2)]
# for i,j in zip(list1,list2):
#     list3.append(i*j)

# list3 = {i:j for(i,j) in zip(list1,list2) }  #for dictionary key value pair is must otherwise it is a set
# print(list3)
# print(type(list3))

# list1 = [26,5,633,23,87,4,9,97,60,44,59,96,25,64]

# def is_prime(n):
#     if n < 2:
#          return False
#     for i in range(2,n): #0 and 1 are not prime and logically every number is divisible by 1 so we start from 2 till the 1 step before that number and if there is any number in that range which can divide the number and left remainder as 0 return false
#         if n % i == 0:
#             return False
#     return True
#
# print("prime numbers are in list1 ")
# for i in list1:
#     if is_prime(i):
#         print(i)

########### ---------concept of multidimensional list ---->> elements of a list has atleast one element as a list itself

# multi_dimensional_list = [[34,89,"ashu"], 88,1,3,4 ,[78,45,20]]
# print(multi_dimensional_list[0][0]) #this is how we can access the list inside of a list
#
# list3 = [[1,2,3],[["a","b","c"],5,6]]
#
# print(list3[1][0][1])


"""   adding items to a list -------------------------------------
method n0.1 append() method -> it adds item in list in the end

syntax:-
list.append(value)
language = ["c", "python", "java"]
language.append("ruby") #append accept exactly on item
# language.append("rust")
# language.append("cobol")
list4 = ["yes","no","true","false"]
language.append(list4)
print(type(language[4]))
print(language)


method no.2 insert() method -> it gives us freedom to add item to anywhere in the list in the beginning or in the middle

syntax:-
list.insert(position,value)

lang_list = ['c', 'python', 'java']
# lang_list.insert(1,'ruby')
lang_list.insert(1,["hubble","bubble"])
print(lang_list)

method no.3 :- extend() method
by this method we can extend a given list to an already created list, because by the use of append and insert the argumented list is seen as an item to the list in which we are passing it

list1 = ["pogo", "cartoon-network", "disnep"]
list2 = ["dell", "microsoft", "apple" ]

list1.extend(list2)
print(list1)
"""


## it split the input sentence by the user , based on the white spaces  and then check whether the value is numerical or not and if yes append it into the list
"""
list1 = []
inp = input("enter the sentence including numbers, strings, characters")
for i in inp.split(" ", 8):
    if i.isnumeric():
        list1.append(int(i))

print(list1)
"""

"""

##input a list using the split() method
number = int(input("how many elements you want"))

numbers = input("enter numbers in one go just entering space between them")

numbers = numbers.split(" ") #if i only do numbers.split() and do not assing to the numbers then it will not overwrite the values and that numbers.split() will not work for the below block of code it will work only for the line in which it is declared
for i in range(0,2):
    numbers[i] = int(numbers[i])

print(numbers)
"""


"""
Q1. Custom Merge and Sort
You are given two strings of numbers separated by commas:

s1 = "9,1,6,3"
s2 = "8,2,5"

🔸 Tasks:

Convert both strings to integer lists using split().
Merge them using extend() (not + operator).
Sort the merged list in ascending order.
Insert the number 10 at the 2nd position (index 1).
Print the final list.


s1 = "9,1,6,3"
s2 = "8,2,5"

s1 = s1.split(",")
s2 = s2.split(",")

new_int_list = []

s1.extend(s2)

i = 0
while i< len(s1):
    s1[i] = int(s1[i])
    new_int_list.append(s1[i])
    i += 1


new_int_list.sort()
new_int_list.insert(1,10)
print(new_int_list)
"""
