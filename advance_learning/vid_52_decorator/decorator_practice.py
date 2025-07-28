from time import sleep

def deco_func(func):                  # STEP 2: Defined and called by @deco_func
    def wrapper_func():              # STEP 5: Inner function defined, not run yet
        print("wrapper_func worked")  # STEP 7: Runs when show() is called
        sleep(3)                      # STEP 8
        return func()                 # STEP 9: Runs the original show()
    print("decorator func_worked")   # STEP 3
    sleep(5)                         # STEP 4
    return wrapper_func              # STEP 6: Returns wrapper_func and replaces show

@deco_func                          # STEP 1: Triggers deco_func(show)
def show():                         # STEP 10: Normal definition, runs later
    print("show worked")            # STEP 11: Runs when func() is called inside wrapper_func

show()                              # STEP 6 again: Now actually runs wrapper_func()



# deco_show = deco_func(show)
# deco_show()    orr just a @deco_func before def show() :- which crate a toll tax from which show function will pass


