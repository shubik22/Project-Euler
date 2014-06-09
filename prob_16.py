def power_sum(n):
  power = 2 ** n
  power_sum = 0
  while power > 0:
    power_sum += power % 10
    power /= 10
  return power_sum
  
print power_sum(1000)