import time
from xml.sax.handler import property_dom_node


def deco_func(func):
    def wrapper_func(*args, **kwargs):
        time.sleep(3)
        print("before show ")
        result = func(*args, **kwargs)
        print("after show ")
        return result
    time.sleep(3)
    print("decorator function worked")
    return wrapper_func

@deco_func
def product(a, b):
    time.sleep(3)
    return a*b


print(product(5,6))



