def fibo_term(n):
 match n:
  case 0: 
   raise ValueError("Fibonacci term 0 does not exist")
  case 1:
   return 0
  case 2: 
   return 1
  case _:
   return fibo_term(n-1) + fibo_term(n-2)

#print(fibo_term(number))
  
def fibo_seq(n):
 return [fibo_term(i) for i in range(1, n+1)]

var = input("Fibonacci : term or seq? ").lower()
if var not in ('term', 'seq'):
 raise ValueError("Invalid choice")
elif var == 'term':
 term = int(input("enter the term you want : "))
 print(fibo_term(term))
else:
 ed = int(input("enter the no of terms you want : "))
 print(fibo_seq(ed))
  