
"""
Why to Use 'if name == main'? :

Code reuse: Ek file ko baar-baar import karna ho to, unwanted code run na ho.

Testing: File ka kuch part sirf testing ke liye likha ho, to wo sirf tab chale jab tum file ko directly run karo.

Cleaner structure: Large projects mein ye best practice hoti hai.

"""
def fact_cal(n):
    if n>0:
        return n* fact_cal(n-1)
    else:
        return 1


#****** ye main block of code maine bana diya hai ye tabhi run hoga jab mai ye wali file tutmain1 run karunga******
if __name__ == '__main__': #this is the main program and only called when we run this program itself
    print(fact_cal(int(input("please enter a number\n"))))
    print("from here")
    print("this function is to find the factorial of a number")
    a= (5+88)
    print(a)

    print("this information is totally redundant")