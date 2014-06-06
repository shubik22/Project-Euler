def square_sum_diff(n):
  return square_of_sums(n) - sum_of_squares(n)

def sum_of_squares(n):
  sum = 0
  for i in range(n):
    sum += (i + 1) ** 2
  return sum
  
def square_of_sums(n):
  sum = n * (n + 1) / 2
  return sum ** 2
  
print square_sum_diff(100)