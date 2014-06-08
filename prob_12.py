def triangle_num_div(n):
  tri_num = 1
  delta = 2
  while divisors(tri_num) < n:
    tri_num += delta
    delta += 1
  return tri_num

def divisors(n):
  divs = list()
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divs.append(i)
      divs.append(n % i)
  return len(divs)
  
print triangle_num_div(500)