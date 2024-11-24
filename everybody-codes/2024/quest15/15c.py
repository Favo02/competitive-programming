import sys
from collections import deque, defaultdict
from heapq import heappush, heappop

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(sx, sy):
  queue = deque([(sx, sy)])
  dist = {(sx, sy): 0}

  while queue:
    x, y = queue.popleft()
    for dx, dy in DIRS:
      nx, ny = x + dx, y + dy
      if not (0 <= nx < len(field[0])):
        continue
      if not (0 <= ny < len(field)):
        continue
      if field[ny][nx] in ('#', '~'):
        continue
      if (nx, ny) in dist:
        continue
      dist[(nx, ny)] = dist[(x, y)] + 1
      queue.append((nx, ny))

  return dist

def dijkstra(start):
  res = float("inf")
  queue = [(0, *start, 0)]
  dist = {(*start, 0): 0}

  while queue:
    d, x, y, found = heappop(queue)

    if d != dist[(x,y,found)]:
      assert d > dist[(x,y,found)]
      continue

    for (nx, ny), wei in graph[(x,y)].items():
      if (nx, ny) == start: continue

      nfound = found
      if (nx, ny) != start:
        nfound = found | (1 << coords_to_index[(nx, ny)])

      if (nx, ny, nfound) in dist and dist[(nx, ny, nfound)] <= d + wei:
        continue

      dist[(nx, ny, nfound)] = d + wei
      heappush(queue, (d + wei, nx, ny, nfound))

      if nfound == (1 << (len(char_to_index))) - 1:
        tohome = d + wei + graph[(nx, ny)][start]
        res = min(res, tohome)

  return res

field = []
start = None
plants = set()

for y, line in enumerate(sys.stdin):
  line = line.strip()
  field.append(line)
  for x, c in enumerate(line):
    if y == 0 and c == ".":
      start = (x, y)
      plants.add((x, y))
    if c.isupper():
      plants.add((x, y))

graph = defaultdict(dict)
dists = {}
for sx, sy in plants:
  for (ex, ey), dist in bfs(sx, sy).items():
    if (ex, ey) in plants:
      graph[(sx, sy)][(ex, ey)] = dist

coords_to_index = {}
char_to_index = {}
for x, y in plants:
  if (x, y) == start: continue

  if field[y][x] in char_to_index:
    coords_to_index[(x, y)] = char_to_index[field[y][x]]
  else:
    coords_to_index[(x, y)] = len(char_to_index)
    char_to_index[field[y][x]] = len(char_to_index)

  assert coords_to_index[(x, y)] == char_to_index[field[y][x]]

dist = dijkstra(start)
print(dist)
