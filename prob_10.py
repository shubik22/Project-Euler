def primes_sum(max):
  i = 2
  primes_sum = 0
  while i < max:
    if is_prime(i):
      primes_sum += i
    i += 1
  return primes_sum

def is_prime(n):
  for i in range (2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
  
print primes_sum(2000000)