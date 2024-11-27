import sys
from collections import deque

def bfs(start):
  queue = deque([(0, *start)])
  seen = set()
  found = 0

  while queue:
    dist, x, y = queue.popleft()

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
      nx, ny = x+dx, y+dy
      if not (0 <= nx < len(field[0])): continue
      if not (0 <= ny < len(field)): continue
      if field[ny][nx] == "#": continue
      if (nx, ny) in seen: continue
      seen.add((nx, ny))

      if (nx, ny) in trees:
        found += 1

      if found == len(trees):
        return dist+1

      queue.append((dist+1, nx, ny))

  assert False

field = []
trees = set()
start = None

for y, line in enumerate(sys.stdin):
  field.append(line.strip())
  for x, cell in enumerate(line.strip()):
    if cell == "." and x == 0:
      start = (x, y)
    if cell == "P":
      trees.add((x, y))

print(bfs(start))
