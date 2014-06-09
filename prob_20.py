from math import factorial

def factorial_sum(n):
  fact = factorial(n)
  return digit_sum(fact)
  
def digit_sum(n):
  digit_sum = 0
  while n > 0:
    digit_sum += (n % 10)
    n /= 10
  return digit_sum
  
print factorial_sum(100)