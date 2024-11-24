import sys
from collections import deque

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

start = None
field = []
plants = set()

for y, line in enumerate(sys.stdin):
  line = line.strip()
  field.append(line)
  if y == 0:
    start = (line.find("."), 0)
  for x, cell in enumerate(line):
    if cell not in [".", "#", "~"]:
      plants.add(cell)

plants = {p: i for i, p in enumerate(plants)}

def bfs(sx, sy):
  start = (0, sx, sy, tuple([False for _ in range(len(plants))]))
  queue = deque([start])
  seen = set()

  while queue:
    d, x, y, pl = queue.popleft()

    for dx, dy in DIRS:
      ax, ay = x+dx, y+dy
      if not (0 <= ax < len(field[0])): continue
      if not (0 <= ay < len(field)): continue
      if field[ay][ax] in ["#", "~"]: continue

      if field[ay][ax] in plants:
        npl = list(pl)
        npl[plants[field[ay][ax]]] = True
        npl = tuple(npl)
      else:
        npl = pl

      if (ax, ay, npl) in seen: continue
      seen.add((ax, ay, npl))

      if all(npl) and (ax, ay) == (sx, sy):
        return ax, ay, d+1

      queue.append((d+1, ax, ay, npl))

  assert False

rx, ry, d = bfs(*start)
print(d)
