def longest_collatz(max):
  longest_collatz = 1
  collatz_dict = dict({1: 1})
  for i in range(1, max + 1):
    temp_i = i
    collatz_len = 0
    while temp_i not in collatz_dict:
      temp_i = next_collatz(temp_i)
      collatz_len += 1
    collatz_dict[i] = collatz_dict[temp_i] + collatz_len
    if collatz_dict[i] > collatz_dict[longest_collatz]:
      longest_collatz = i
  return longest_collatz

def next_collatz(n):
  if n % 2 == 0:
    return n/2
  else:
    return 3 * n + 1
    
print longest_collatz(1000000)