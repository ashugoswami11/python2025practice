"""
Ques 1. Simple Greeter Coroutine
Ek coroutine banao greeter() jo continuously name receive kare aur print kare "Hello, {name}".


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


Ques 2. Running Average Calculator
Ek coroutine banao jo numbers receive kare aur unka running average calculate kare.
Har bar jab number bhejo, wo average return kare.

def Running_average():
    list1 = []
    while True:
        num = (yield)
        list1.append(num)
        average = sum(list1) / len(list1)
        print(average)

inst = Running_average()
next(inst)

inst.send(5)
inst.send(15)
inst.send(34)
inst.send(87)
inst.send(56)


Ques 3. Word Filter Coroutine
Ek coroutine banao jo continuously sentence receive kare aur agar sentence me "error" word aata hai
toh "Alert: Error found!" print kare, warna "All good!".
"""

def error_checker():
    while True:
        sentence = (yield)
        let = True
        for word in sentence.split():
            if word in ("Error","error"):
                let = False
                print("Alert: Error found!")
                break
        if let:
            print("All good")
            break


inst = error_checker()
next(inst)
inst.send("heyy there are you okay")









