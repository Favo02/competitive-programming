import sys

adj = [(0,-1), (0,+1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

def recPath(start, target, paths):
  path = []
  while target != start:
    path.append(paths[target])
    target = paths[target]
  return path

def bfs(start, target):
  prec = {start:-1}
  queue = [start]

  while queue:
    cur = queue.pop(0)

    if cur == target:
      break

    for a in adj:
      next = (cur[0] + a[0], cur[1] + a[1])

      if next[0] > gridSize or next[0] < 0:
        continue
      if next[1] > gridSize or next[1] < 0:
        continue
      # print(next[0], next[1])
      if next[0] == gridSize or next[1] == gridSize or grid[next[1]][next[0]] == "W":
        if next not in prec:
          prec[next] = cur
          queue.append(next)

  return prec

diagComple = {
  (1,-1): ((0,-1),(1,0)),
  (1,1): ((0,1),(1,0)),
  (-1,1): ((-1,0),(0,1)),
  (-1,-1): ((-1,0),(0,-1)),
}

input = sys.argv[1]
f = open(input, "r")
lines = list(map(lambda l: l[:-1], f.readlines()))
gridSize = int(lines[0])
grid = lines[1:1+gridSize]
coords = list(map(lambda t: t.split(" "), lines[1+gridSize:][1:]))
# print(coords)
for c in coords:
  a = c[0].split(",")
  b = c[1].split(",")
  x1, y1 = int(a[0]), int(a[1])
  x2, y2 = int(b[0]), int(b[1])
  target = (x1, y1)
  start = (x2, y2)
  paths = bfs(start, target)
  path = recPath(start, target, paths)
  path.insert(0, target)
  print(f"{path[0][0]},{path[0][1]}", end="")
  for i in range(1, len(path)):
    p = path[i]
    print(f" {p[0]},{p[1]}", end="")
  print("")


