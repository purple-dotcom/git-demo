
mylist = ['apple','banana','orange','grape']
'''
x = mylist
y = mylist.copy()
print(x)
print(y)
'''

mytuple = tuple(mylist)
fruits = mytuple * 2
print(fruits)
print(type(fruits))
#print(instanceOf(tuple, fruits))
print(id(fruits), id(mytuple))