"""
Ques 1. ATM Machine Simulation
Ek function banao jo user se paisa withdraw kare.
Agar user balance se zyada paisa nikalne ki koshish kare toh ValueError raise karo.
Agar koi error nahi aati toh else block me "Withdrawal Successful" print karo.
Chahe error aaye ya na aaye, finally block me "Thank you for using our ATM!" print karo.

bank_balance = 10000
def Atm_machine(n):
    try:
        if n > bank_balance:
            raise ValueError("Insufficient balance")
        else:
            print("Withdrawal Successful")
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for using our ATM!")

Atm_machine(100000)


Ques 2.
Division Calculator
Ek program banao jo user se do numbers input kare aur divide kare.
Agar denominator 0 ho toh error handle karo.
Agar error nahi aayi toh else me result print karo.
finally me "Operation Complete" print karo.

def Division_cal(n1, n2):
    try:
        if n2 == 0:
            raise ZeroDivisionError("can not divide by zero")
        else:
            return n1 / n2
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Operation Completed")


print("enter numerator")
n1= int(input())
print("enter denominator")
n2 = int(input())

print("division result is ", Division_cal(n1, n2))

Ques 3. File Handling Practice
Ek file open karke usme read karne ki koshish karo.
Agar file exist nahi karti toh exception handle karo.
Agar file sahi se open ho gayi toh else me file ke contents print karo.
Aur chahe jo bhi ho, finally me file close karna ensure karo.
"""
from basic_learning.module_use_fstring import bank_balance


def file_handler():
    file = None
    try:
        file = open("example.txt", "r")
        content = file.read()
    except FileNotFoundError as e:
        print(e)
    else:
        print(content)
    finally:
        file.close()
        print("file is closed program is successful")

file_handler()

