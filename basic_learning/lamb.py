""" lambda or anonymous functions are one-liner functions which usually perform a single task
 or we can say a single expression
 lambda function can be passed as an argument in a function

 example :--
 double = lambda x: x*2

------------------------------------------------------------------------------------

# ------ filter---------

num_list = [2,7,23,8,45,36,76,20]

even_num_list = list(filter(lambda x: x%2==0 ,num_list))  #filter(function,iterable)


#---------map------------
doubles = list(map(lambda x : x*2 ,even_num_list ) ) #map(function, iterables)


#---------reduce------------
from functools import reduce
sum_doubles = reduce(lambda x,y : x+y,doubles) #reduce(function, iterables)
print(sum_doubles)

 ---------------------------------------------------------------------------
 """

from functools import reduce
fact = lambda n: reduce(lambda x,y : x*y, range(1,n+1)) if n > 0 else 1
print(fact(5))

# list = [[66,3], [7,55],[23,5]]
# # list.sort(key = lambda x : x[1])
# list.sort(key = lambda x : x[1])  #here key means on what basis you want to sort
# print(list)
