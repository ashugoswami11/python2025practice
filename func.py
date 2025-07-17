def averagecal(a, b):
    """this function is used to calculate the average of two numbers"""   #this is how a doctype is declared inside the function at the very first line
    average = (a+b)/2
    return average

v = averagecal(2,5)
print("average of two numbers is ", v)
print(averagecal.__doc__)    #this is the way to find the doctype of function. Doc type is basically very first line inside the function which tell about the function

#function in python can be used in several ways like if we're including something in the function or our program which require changes very often then we have to make change in our function only rather than in whole program and all the programs which are calling that function automatically synchronize