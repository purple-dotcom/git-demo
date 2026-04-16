set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print(set1.symmetric_difference(set2))
set3 = set1.symmetric_difference(set2)
print(id(set1) == id(set3))