import time
#prob 1:--
"""
def UPPERCASE_deco(func):
    def wrapper(*args, **kwargs):
        print("wrapper function")
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        else:
            print("can't handle anything execpt string")
        return result

    return wrapper


@UPPERCASE_deco
def greeting(name):
    return name

@UPPERCASE_deco
def product(a, b):
    return a * b

print(greeting("Bob"))
print(product(4, 2))
"""

#prob 2:----

def deco_time(func):
    def inner_deco(*args, **kwargs):
        print("----------start----------")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("----------end----------")
        print("\n")
        print(f"this function {func.__name__} takes: {end - start:.12f} seconds" )
        return result
    return inner_deco

@deco_time
def func2(name, age):
    print(f"hello {name}, you are {age} years old")

func2("Ashu", 25)