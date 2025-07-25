#-- working on the water alert
import time

current_local_time = time.strftime("%H:%M",time.localtime())
print(current_local_time)


# while True:
#     current_local_time = time.strftime("%H:%M", time.localtime())
#     if "5:00" < current_local_time < "12:00":
#         print("good morning")
