def smallest_multiple(n):
  if n == 1:
    return 1
  else:
    prev_mult = smallest_multiple(n - 1)
    temp_prev_mult = prev_mult
    factor = 2
    while factor <= n:
      if n % factor == 0 and temp_prev_mult % factor == 0:
        n /= factor
        temp_prev_mult /= factor
        factor = 2
      else:
        factor += 1
    return prev_mult * n
    
print smallest_multiple(20)