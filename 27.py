import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

y = re.search("ai", txt)
print(y) #this will print an object