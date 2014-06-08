def special_pythag(n):
  for b in range(1, n):
    for a in range(1, b):
      if pythag_sum(a, b) == n:
        return a * b * (n - a - b)
  
def pythag_sum(a, b):
  c = (a ** 2 + b ** 2) ** (0.5)
  return a + b + c
  
print special_pythag(1000)