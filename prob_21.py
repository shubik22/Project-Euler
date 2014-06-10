def amicable_sum(max):
  amicable_sum = 0
  for i in  range(2, max + 1):
    if div_sum(div_sum(i)) == i and div_sum(i) != i:
      amicable_sum += i
  return amicable_sum

def div_sum(n):
  divisor_sum = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisor_sum += (i + n/i) if (n/i != i) else i
  return divisor_sum - n

print amicable_sum(10000)