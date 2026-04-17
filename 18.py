def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

def fibonacci_seq(n):
    if not isinstance(n,int):
        raise ValueError("n must be an integer!")
    if n < 1:
        raise ValueError("n must be >= 1")
    
    a, b = 0, 1
    seq = []
    for _ in range(n-1):
        seq.append(a)
        a,b = b, a+b
    return seq