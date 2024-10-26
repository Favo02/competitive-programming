def valid(row, col):
  for rr in grid[row]:
    if rr == "#":
      return False
  for cc in range(8):
    if grid[cc][col] == "#":
      return False
  return True

grid = []
for r in range(8):
  grid.append(input())

res = 0
for r in range(8):
  for c in range(8):
    if valid(r, c):
      res += 1

print(res)
