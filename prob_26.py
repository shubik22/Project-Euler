def best_cycle(max_val):
  best_cycle = 0
  best_denom = 0
  for denom in range(2, max_val + 1):
    cycle = rep_cycle(denom)
    if cycle > best_cycle:
      best_cycle, best_denom = cycle, denom
  return best_denom
  
def rep_cycle(denom):
  remainder = 10
  remainders = {} # key is remainder, value is digit spot
  digit = 0
  while remainder > 0:
    digit += 1
    if remainder in remainders:
      return digit - remainders[remainder]
    else:
      remainders[remainder] = digit
      remainder = (remainder % denom) * 10
  return 0

print best_cycle(1000)