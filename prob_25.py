def fib_num(digits):
  fib_a = 1
  fib_b = 1
  fib_count = 2
  while fib_b < (10 ** (digits - 1)):
    fib_a, fib_b = fib_b, fib_a + fib_b
    fib_count += 1
  return fib_count
  
print fib_num(1000)