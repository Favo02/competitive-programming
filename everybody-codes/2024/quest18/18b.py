import sys
from collections import deque

def bfs(starts):
  queue = deque([(0, *s) for s in starts])
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

      if field[ny][nx] == "P":
        found += 1

      if found == trees:
        return dist+1

      queue.append((dist+1, nx, ny))

  assert False

field = []
trees = 0
starts = []

for y, line in enumerate(sys.stdin):
  field.append(line.strip())
  for x, cell in enumerate(line.strip()):
    if cell == "." and x == 0:
      starts.append((x, y))
    if cell == "." and x == len(field[0])-1:
      starts.append((x, y))
    if cell == "P":
      trees += 1

print(bfs(starts))
