## agenda :-- code a snake water gun game
"""
giving 10 chances to the user to play
computer = random function , user input
after 10 games final winner decided

-------------------------------
precedences
water,snake = snake
water,gun = water
snake,gun = gun
same,same = tie
"""
import random as rand

from django.utils.translation import trim_whitespace

list = ["snake", "water", "gun"]
counter = 10

score_user = 0
score_computer = 0

while (counter>0):
    print("chances left: ",counter)
    comp_choice = rand.choice(list)

    user_inp = trim_whitespace(input(f"enter your choice:--{"snake, "}{"water, "}{"gun"}\n"))

    if user_inp == comp_choice:
        print("it's a tie!")
        score_computer +=1
        score_user +=1

    elif (user_inp,comp_choice) in [("snake","water"),("water","snake")]:
        if user_inp ==  "snake":
            print("user won")
            score_user += 1
        else:
            print("computer won")
            score_computer += 1

    elif (user_inp, comp_choice) in [("gun", "water"), ("water", "gun")]:
        if user_inp == "water":
            print("user won")
            score_user += 1
        else:
            print("computer won")
            score_computer += 1

    elif(user_inp, comp_choice) in [("snake", "gun"), ("gun", "snake")]:
        if user_inp == "gun":
            print("user won")
            score_user += 1
        else:
            print("computer won")
            score_computer += 1

    else:
        print("invalid input")

    counter -= 1
    if counter == 0:
        print("\ngame end\n")



if score_computer == score_user:
    print("this whole game is tie")

elif score_computer > score_user:
    print("your score is", score_user,
          "computer score is", score_computer)
    print("*****computer won*****")

else:
    print("your score is", score_user,
          "computer score is", score_computer)
    print("*****user won*****")



