def path_sum(filename):
  tri = parse_file(filename)
  for row in reversed(range(0, len(tri))):
    if row == 0:
      return tri[0][0]
    for col in range(0, len(tri[row]) - 1):
      tri[row - 1][col] += max(tri[row][col], tri[row][col + 1])

def parse_file(filename):
  tri_str = open(filename, "r").read()
  triangle = tri_str.split("\n")
  for i in range(0, len(triangle)):
    triangle[i] = triangle[i].split(" ")
    for j in range (0, len(triangle[i])):
      triangle[i][j] = int(triangle[i][j])
  return triangle
  
print path_sum("prob_67.txt")