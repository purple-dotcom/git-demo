def func(n):

    def inner(a):
        return a * n

    return inner


double = func(2) #returns inner(2)
triple = func(3) #returns inner(3)
quadruple = func(4) #returns inner(4)

print(double(10))
print(triple(10))
print(quadruple(10))
print('version1')