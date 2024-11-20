import sys
from heapq import heappush, heappop

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def hdiff(x1, y1, x2, y2):
  h1 = field[y1][x1]
  h2 = field[y2][x2]
  return min(abs(h1 - h2), 10 - h1 + h2, 10 - h2 + h1)

def dijkstra(start):
  queue = []
  dists = {}

  queue.append((0, *start))
  dists[start] = 0

  while queue:
    cdist, cx, cy = heappop(queue)

    for dx, dy in DIRS:
      ax, ay = cx + dx, cy + dy

      if not (0 <= ax < len(field[0])): continue
      if not (0 <= ay < len(field)): continue
      if field[ay][ax] == "#": continue

      newdist = 1 + cdist + hdiff(cx, cy, ax, ay)
      if (ax, ay) == end:
        return newdist

      if (ax, ay) in dists and dists[(ax, ay)] <= newdist:
        continue

      dists[(ax, ay)] = newdist
      heappush(queue, (newdist, ax, ay))

  return dists

field = []
starts = []
end = None

for y, line in enumerate(sys.stdin):
  line = line.strip()
  field.append([int(c) if c.isdigit() else c for c in line])

  for x, cell in enumerate(line):
    if cell == "S":
      starts.append((x, y))
      field[y][x] = 0
    if cell == "E":
      end = (x, y)
      field[y][x] = 0

res = float("inf")
for i, s in enumerate(starts):
  res = min(res, dijkstra(s))

print(res)
