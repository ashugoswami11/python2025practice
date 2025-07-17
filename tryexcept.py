print("enter first number")
num1 = int(input())
print("enter second number")
num2 = int(input())

try:
    print("division of two numbers is", num1/num2)
except Exception as e:
    print(e,"error")

    #this is how exception handling works easy and simple just put your error-prone code into try block followed by except block and do it as above

    # with this way it simply converts the error into a harmless error message and help program to not get crash