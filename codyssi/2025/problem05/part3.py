import sys

def bfs(start):
  seen = set()
  path = 0
  while True:
    dist, coord = closest(start, seen)
    seen.add(coord)
    path += dist
    start = coord
    if len(seen) == len(islands):
      break
  return path

def mdist(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def closest(start, seen):
  mindist = float("inf")
  mincoor = (float("inf"), float("inf"))
  for a, b in islands:
    if (a, b) in seen:
      continue
    dist = mdist(*start, a, b)
    if dist < mindist:
      mindist = dist
      mincoor = (a, b)
    elif dist == mindist:
      mincoor = min(mincoor, (a, b))
  return mindist, mincoor

lines = list(map(str.strip, sys.stdin.readlines()))
islands = []

for line in lines:
  a, b = line.split(", ")
  a = int(a[1:])
  b = int(b[:-1])
  islands.append((a, b))

res = bfs((0,0))
print(res)
