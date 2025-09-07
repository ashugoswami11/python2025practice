"""
Ques 1. Simple Greeter Coroutine
Ek coroutine banao greeter() jo continuously name receive kare aur print kare "Hello, {name}".
"""

from time import sleep
def greeter1():
    greeting = "hello"
    sleep(3)
    print("loading successful")

    while True:
        result=(yield)
        print(greeting, result)

search = greeter1() #assembler
print("greeter getting ready")
next(search) # standby mode
search.send("ashu")

