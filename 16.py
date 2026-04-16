def func1(): 
 print(func1.__name__) 
a = func1 
a()
print(a.__name__)
#therefore, a() exists as a function. Because a and func both point to the same function object.

print('~~~~~~~~~~~~~~~~~~~~~~')

def func2(n): 
 print(func2.__name__)
 return n * 5
b = func2 
print(b(3))
print(b.__name__)
#therefore, b(n) exists and has an argument. 

print('~~~~~~~~~~~~~~~~~~~~~~~~~')
def func3(n): 
 def nested_func(p): 
  return p * n 
 print(func3.__name__)
 return nested_func 

c = func3(2)
print(c(10))
print(c.__name__)

#c points to nested_func with n remembered.
