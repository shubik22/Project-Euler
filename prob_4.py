def three_digit_palindrome():
  solution = 0
  for i in range(100, 1000):
    for j in range(i, 1000):
      product = i * j
      if (product > solution) and is_palindrome(i * j):
        solution = i * j
  return solution

def is_palindrome(n):
  int_str = str(n)
  mid_idx = (len(int_str)) // 2
  for i in range(mid_idx):
    if int_str[i] != int_str[-(1 + i)]:
      return False
  return True
  
print three_digit_palindrome()