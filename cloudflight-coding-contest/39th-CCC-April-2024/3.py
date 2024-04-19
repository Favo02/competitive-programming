def due(path):
  x, y = 0, 0
  maxx, minx = 0, 0
  maxy, miny = 0, 0

  for s in path:
    if s not in dir: continue
    dx, dy = dir[s]
    x, y = x+dx, y+dy

    maxx = max(maxx, x)
    minx = min(minx, x)

    maxy = max(maxy, y)
    miny = min(miny, y)

  return maxx, minx, maxy, miny

def prgr(grid):
  for r in grid:
    print("".join(r))

def solve():

  width, height = [int(n) for n in input().split()]
  grid = []

  for _ in range(height):
    grid.append(list(input().rstrip()))

  path = input()

  maxx, minx, maxy, miny = due(path)

  if maxx-minx +1 != width:
    return False
  if maxy - miny +1 != height:
    return False


  x, y = abs(minx), abs(miny)

  if grid[y][x] == "X":
    return False

  # print(grid)
  # print(x, y)

  count = 1
  if not (0 <= x < width):
    return False

  if not (0 <= y < height):
    return False
  grid[y][x] = "P"

  for s in path:
    # print(grid)
    if s not in dir: continue
    dx, dy = dir[s]
    x, y = x+dx, y+dy

    if not (0 <= x < width):
      return False

    if not (0 <= y < height):
      return False

    if grid[y][x] == "X":
      return False

    if grid[y][x] == "P":
      return False

    grid[y][x] = "P"
    count += 1


  if (width * height) -1 != count:
    return False
  return True


paths = int(input())
dir = {"W":(0, -1), "S":(0, 1), "D":(1,0), "A":(-1, 0)}

for _ in range(paths):
  if solve():
    print("VALID")
  else:
    print("INVALID")



