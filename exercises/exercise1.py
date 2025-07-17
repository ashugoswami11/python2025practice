import random as rand

num1 = rand.randint(1,100)

i = 0
counter = 9
print("welcome to the number guess game")

while counter > i:
    print("enter a number")
    user_input = int(input())

    if user_input == num1:
        print("congrats you won")
        print("you completed the game in ", i+1, "th attempt")
        break

    elif num1 < user_input:
        if user_input - num1 < 5 :
            print("you are too close try with smaller")
        else:
            print("you entered bigger number")

    elif num1 > user_input:
        if num1 - user_input < 5:
            print("you are too close try with bigger")
        else:
            print("you entered small number")

    print("chances left ",counter )

    i = i + 1
    counter = counter - 1
