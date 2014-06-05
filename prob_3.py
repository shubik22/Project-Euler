def largest_factor(n):
  solution = 1
  factor = 2
  while n > 1:
    if n % factor == 0:
      n /= factor
      solution = max(solution, factor)
      factor = 2
    else:
      factor += 1
  return solution
  
print largest_factor(600851475143)