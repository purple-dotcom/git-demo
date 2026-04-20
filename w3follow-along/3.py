x = 1
#x :=3
print(x:=3)

a = 3
b = 3
print(a is b)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
for i in thislist:
	print(i, end=' ')
print()
dict = {1:"bombardilo", 2:"crocodilo"}
thislist.extend(dict)
print(thislist)