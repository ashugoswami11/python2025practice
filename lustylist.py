groccery = ["books", "lemon", "harpic", "salt"]
print(type(groccery))

numlist = [34,34,5,6,76,66,34]
# numlist.sort() #it works outside the print statement
numlist.pop()
print(numlist)

print(groccery[0][0:3])
print(max(groccery)) #for the list of string items max and min give the result in the form of the index number not in the biggest or smallest
groccery.append("soybean")  #it also works outside the print statement
print(groccery)

#tuples are initiated with the parenthesis
#list can contains many methods whereas tuples have fewer
tup= (45,34,23,"haary")
tup1=("miss", "oxford", "mit")

print(tup)
print(tup1.count("oxford"))
print(tup1.index("mit"))
tup2= (1,)  #to make the tuple of one item we have to put a comma after the value so that compiler understand it as a tuple not a value inside   parenthesis

# swapping 2 numbers
a=9
b=7
a,b = b,a
print(a,b)
groccery.extend(numlist)
print(groccery)