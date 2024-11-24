import sys
from collections import deque

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]


start = None
field = []
for y, line in enumerate(sys.stdin):
  line = line.strip()
  field.append(line)
  if y == 0:
    start = (line.find("."), 0)

print(field)

def bfs(start):
  queue = deque([start])
  dist = {start: 0}

  while queue:
    x, y = queue.popleft()
    print(x, y)

    for dx, dy in DIRS:
      ax, ay = x+dx, y+dy
      if not (0 <= ax < len(field[0])): continue
      if not (0 <= ay < len(field)): continue
      if field[ay][ax] == "#": continue
      if (ax, ay) in dist: continue

      if field[ay][ax] == "H": return dist[(x, y)] + 1

      dist[(ax, ay)] = dist[(x, y)] + 1
      queue.append((ax, ay))

  assert False

print(bfs(start)*2)
