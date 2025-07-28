# for i in range(1,100):
#     if i % 3 ==0 or i%5 == 0:
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1
#     if i == 100:
#         break
#

while True:
    num = int(input("enter a number\n"))
    if num < 100 :
        print("you entered a small number")
        continue
    if num > 100 :
        print(" congratulations you entered a large number")
        break

