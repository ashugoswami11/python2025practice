import random
import random as rd
import math

list=[1,2,3,4,5,6]

dice_number = rd.choice(list)  #choice is a widely used random module's method
print("\t \t \t ludo dice number\t \t \t")

print("dice number is",dice_number)
print("square of dice number",math.pow(dice_number,2))

print(math.factorial(5))
print(random.random())


#-----------F-Strings-----------
### fstrings are used in string formatting in python. It makes convenient to add variables inside a string either string or integers
place = "delhi"
name = "ashu"
pin  = 110094
bank_balance = 1200.9809238849
print(f"my name is {name}. i live in {place} pincode is {pin}. My bank balance is {bank_balance:.2f}")