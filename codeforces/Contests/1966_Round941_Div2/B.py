def solve():
  rows, cols = [int(n) for n in input().split()]
  grid = []
  for _ in range(rows):
    grid.append(input().rstrip())
    assert(len(grid[-1]) == cols)

  # for color in ['W', 'B']:
  #   min_hei, max_hei = -1, -1
  #   min_row, max_row = -1, -1

  if ('W' in grid[0]) and ('W' in grid[-1])\
      and ('W' in [row[-1] for row in grid])\
      and ('W' in [row[0] for row in grid]):
    return True

  if ('B' in grid[0]) and ('B' in grid[-1])\
      and ('B' in [row[-1] for row in grid])\
      and ('B' in [row[0] for row in grid]):
    return True

  return False

cases = int(input())
for _ in range(cases):
  if solve():
    print("YES")
  else:
    print("NO")
