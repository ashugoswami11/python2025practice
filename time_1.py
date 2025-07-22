import time

# More accurate timer
initial = time.perf_counter()
for i in range(1000000):
    x = i * i
for_duration = (time.perf_counter() - initial)/1000000
print("Time taken by for loop:", for_duration)

initial2 = time.perf_counter()
k = 0
while k < 1000000:
    x = k * k
    k += 1
while_duration = (time.perf_counter() - initial2)/1000000
print("Time taken by while loop:", while_duration)

# Comparison
if for_duration > while_duration:
    print("For loop took more time.")
elif for_duration < while_duration:
    print("While loop took more time.")
else:
    print("It's a tie.")

local = time.asctime(time.localtime(time.time()))
print(local)