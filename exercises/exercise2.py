# printing star patterns

#range() arguments are passed  in this way (start , stop , step )

user_input = int(input("enter a number\n"))

print("enter 1 for star pyramid and 0 for reverse star pyramid")
user_input1 = bool(int(input()))

if user_input1 == True:
    for i in range(1,user_input+1):
        for j in range(1,i+1):
            print("*", end="")  #because I don't want to jump onto next line right after the the 1 star print in inner loop , i have to wait until whole line print
        print()

elif user_input1 == False:
    for i in range(user_input,0,-1):
        for j in range(1,i+1):
            print("*", end= "")
        print()


