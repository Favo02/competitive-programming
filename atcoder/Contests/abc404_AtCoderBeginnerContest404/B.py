def pprint(grid):
  for g in grid:
    print(g)
  print()

def rotate_90(grid):
  return ["".join(row) for row in zip(*reversed(grid))]

def diff(g1, g2):
  count = 0
  for a, b in zip(g1, g2):
    for aa, bb in zip(a, b):
      if aa != bb:
        count += 1
  return count

N = int(input())

grid1 = []
for _ in range(N):
  grid1.append(input())

grid2 = []
for _ in range(N):
  grid2.append(input())

res = diff(grid1, grid2)

for i in range(3):
  grid1 = rotate_90(grid1)
  res = min(res, i+1 + diff(grid1, grid2))

print(res)
