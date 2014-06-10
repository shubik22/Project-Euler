def triangle_words(filename):
  words = open(filename, "r").read().replace("\"", "").split(',')
  count = 0
  for word in words:
    if triangle_word(word):
      count += 1
  return count

def triangle_word(word):
  val = word_value(word)
  return ((1 + 8 * val) ** 0.5 - 1) % 2 == 0

def word_value(word):
  word_value = 0
  for i in range(0, len(word)):
    word_value += ord(word[i]) - 64
  return word_value

print triangle_words("prob_42.txt")