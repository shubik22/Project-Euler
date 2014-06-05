def even_fib_sum(n):
  sum = 0
  fib_a, fib_b = 1, 2
  while fib_b < n:
    if fib_b % 2 == 0:
      sum += fib_b
    fib_a, fib_b = fib_b, fib_a + fib_b
  return sum

print even_fib_sum(4000000)