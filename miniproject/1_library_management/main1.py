from admin_login import admin_func
from member import member_func

print("are you admin or member press 1,2 respectively")
ch1 = int(input())
if ch1 == 1:
    admin_func()

elif ch1 == 2:
    member_func()