import sys
from heapq import heappop, heappush

def dist(r1, c1, r2, c2):
  return abs(r1-r2) + abs(c1-c2)

def prim(stars):
  queue = [(0, *stars[0])]
  taken = set()

  res = 0

  while queue:
    d, r, c = heappop(queue)
    if (r, c) in taken: continue
    taken.add((r, c))

    res += d

    for ar, ac in stars:
      if (ar, ac) in taken: continue
      heappush(queue, (dist(r, c, ar, ac), ar, ac))

  return res

stars = []
for r, line in enumerate(sys.stdin):
  for c, cell in enumerate(line.strip()):
    if cell == "*":
      stars.append((r, c))

print(len(stars) + prim(stars))

