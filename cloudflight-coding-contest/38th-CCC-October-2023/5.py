import sys

adjsea = [(0,-1), (0,+1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
adj = [(0,-1), (0,+1), (1,0), (-1,0)]

def isAdj(p1, p2):
  for a in adjsea:
    if (p1[0] + a[0], p1[1] + a[1]) == p2:
      return True
  return False

def dfsIsland(start):
  
  sea = set()
  visited = set()
  queue = [start]

  while queue:
    cur = queue.pop(0)

    for a in adj:
      newx = cur[0]+a[0]
      newy = cur[1]+a[1]

      if newx >= gridSize or newx < 0: continue
      if newy >= gridSize or newy < 0: continue

      type = grid[newy][newx]
      
      if type == "L" and (newx, newy) not in visited:
        queue.append((newx, newy))
        visited.add((newx, newy))
      elif type == "W":
        sea.add((newx, newy))

  return sea

input = sys.argv[1]
f = open(input, "r")
lines = list(map(lambda l: l[:-1], f.readlines()))
gridSize = int(lines[0])
grid = lines[1:1+gridSize]
coords = list(map(lambda t: t.split(","), lines[1+gridSize:][1:]))
# print(coords)

for c in coords:
  x = int(c[0])
  y = int(c[1])

  route = list(dfsIsland((x,y)))
  # print(route)

  path = [ route[0] ]

  route = route[1:]
  while route:
    # print(route)
    cur = path[-1]
    for i in range(len(route)):
      if isAdj(cur, route[i]):
        # print(path)
        path.append(route[i])
        break
    route = route[:i] + route[i+1:]

  print(f"{path[0][0]},{path[0][1]}", end="")
  for i in range(1, len(path)):
    p = path[i]
    print(f" {p[0]},{p[1]}", end="")
  print()

