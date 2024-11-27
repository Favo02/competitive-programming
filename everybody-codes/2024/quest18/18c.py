import sys
from collections import deque

def bfs(start, curbest):
  queue = deque([(0, *start)])
  seen = set()
  found = 0
  res = 0

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
        res += dist+1
        found += 1

      if res >= curbest:
        return float("inf")

      if found == trees:
        return res

      queue.append((dist+1, nx, ny))

  assert False

field = []
trees = 0
starts = []

for y, line in enumerate(sys.stdin):
  field.append(line.strip())
  for x, cell in enumerate(line.strip()):
    if cell == ".":
      starts.append((x, y))
    if cell == "P":
      trees += 1

res = float("inf")
for i, s in enumerate(starts):
  res = min(res, bfs(s, res))
print(res)
