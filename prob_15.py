from math import factorial

def num_paths(n):
  return factorial(2 * n)/(factorial(n) ** 2)

print num_paths(20)