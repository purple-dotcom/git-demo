def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen),end=' ')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# List comprehension
# x,y = 0,1
# seq = []
# for i in range(100):
#   seq.append(x)
#   x,y = y, x+y
# print(seq)

#simple loop
# a,b = 0,1
# for x in range(100):
#   print(a,end=' ')
#   a,b = b,a+b