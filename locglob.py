# val = 5
#
# def func():
#     # val = 10
#     global val  #global keyword is mandatory to use for modification
#     val = val +4  #this type of modification in not directly allowed inside the function
#     print(val)
#
#
# func()
x = 77
def first():
    x = 20
    def second():
        global x
        x = 30
    print("before calling second()", x)
    second()
    print("after calling second()", x)

print(x)
first()
print(x)