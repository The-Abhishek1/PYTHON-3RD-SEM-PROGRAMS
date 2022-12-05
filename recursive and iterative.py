#Recursive approach:

def fibonacci_recursive(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
  
print("Fibonacci series using Recursive function","\n")
for i in range(5):
  print(fibonacci_recursive(i))

print("\n""Fibonacci series using Iteration ","\n")

#Iterative approach:

def fibonacci_iterative(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    a = 0
    b = 1
    for i in range(2, n+1):
      c = a + b
      a = b
      b = c
    return b

for i in range(10):
  print(fibonacci_iterative(i))

