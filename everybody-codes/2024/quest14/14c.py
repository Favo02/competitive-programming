import sys
from collections import deque

DIRS = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

def leafs_dist(x, y, z):
  dists = bfs(x, y, z)
  res = 0
  for lx, ly, lz in leafs:
    if (lx, ly, lz) not in dists:
      return float("inf")
    res += dists[(lx, ly, lz)]
  return res

def bfs(sx, sy, sz):
  queue = deque()
  queue.append((sx, sy, sz))
  dists = {}
  dists[(sx, sy, sz)] = 0

  while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in DIRS:
      ax = x+dx
      ay = y+dy
      az = z+dz
      if (ax, ay, az) not in seen: continue
      if (ax, ay, az) in dists: continue
      dists[(ax, ay, az)] = dists[(x, y, z)] + 1
      queue.append((ax, ay, az))

  return dists

seen = set()
leafs = []
height = 0

for line in sys.stdin:
  steps = line.strip().split(",")

  x = y = z = 0
  for s in steps:
    dir, qty = s[0], int(s[1:])

    dx = dy = dz = 0
    if dir == "U": dy = 1
    if dir == "D": dy = -1
    if dir == "R": dx = 1
    if dir == "L": dx = -1
    if dir == "F": dz = 1
    if dir == "B": dz = -1

    for _ in range(qty):
      x += dx
      y += dy
      z += dz
      seen.add((x,y,z))

    if x == 0 and z == 0:
      height = max(height, y)

  leafs.append((x,y,z))

res = 1e9
for i in range(height+1):
  res = min(res, leafs_dist(0, i, 0))

print(res)
