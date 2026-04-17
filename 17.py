def countdown(n):
  if n == 0:
    print('ZERO!!')
  else: #kamehameha
    print(n)
    countdown(n - 1)


countdown(5)

def fibonacci(n):
  if not isinstance(n,int):
    raise ValueError("enter integer!")
  if n < 1:
    raise ValueError("n must be >= 1")
  
  a, b = 0,1
  for _ in range(n-1):
    a, b = b, a+b
  return a