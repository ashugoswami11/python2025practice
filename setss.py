
#sets hold unordered and unrepetitive items

#set is initialize by the curly brackets but unlike dictionary it doesn't have key value pairs
s = {23,6,12,2}
b = {64,77,12,6}
t = {45,2,8,6}

sb = s.union(b,t)    #union as well as intersection both works in same manner like this
print(sb)