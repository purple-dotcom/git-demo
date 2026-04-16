def outer():
    print("outer runs")
    def inner():
        print("inner runs")
    
    return inner    # returning the function object, not calling it

my_func = outer()   # outer() runs, returns inner (not its result)
my_func()           # now we call inner
# inner runs

#print(my_func)
#print(outer)