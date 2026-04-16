def myfunc1():
  x = "Jane" 
  print(x)
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())