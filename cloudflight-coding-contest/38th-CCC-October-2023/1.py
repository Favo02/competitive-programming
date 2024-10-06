import sys

input = sys.argv[1]
f = open(input, "r")
lines = list(map(lambda l: l[:-1], f.readlines()))
gridSize = int(lines[0])
grid = lines[1:1+gridSize]
coords = list(map(lambda t: t.split(","), lines[1+gridSize:][1:]))
# print(grid)
# print(coords[1:])
for c in coords:
  a = int(c[0])
  b = int(c[1])
  res = grid[b][a]
  print(res)
