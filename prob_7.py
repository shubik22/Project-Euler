def nth_prime(n):
  num = 1
  count = 0
  while count < n:
    num += 1
    if is_prime(num):
      count +=1
  return num

def is_prime(n):
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
  
print nth_prime(10001)