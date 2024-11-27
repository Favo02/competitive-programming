import sys
from heapq import heappop, heappush
from functools import reduce

def dist(r1, c1, r2, c2):
  return abs(r1-r2) + abs(c1-c2)

def prim(stars):
  queue = [(0, *stars.pop())]
  taken = set()

  res = 0

  while queue:
    d, r, c = heappop(queue)
    if (r, c) in taken: continue
    taken.add((r, c))

    res += d

    for ar, ac in stars:
      if (ar, ac) in taken: continue
      d = dist(r, c, ar, ac)
      if d >= 6: continue
      heappush(queue, (d, ar, ac))

  return res, taken

stars = set()
for r, line in enumerate(sys.stdin):
  for c, cell in enumerate(line.strip()):
    if cell == "*":
      stars.add((r, c))

const = []

while len(stars) > 0:
  res, taken = prim(stars)
  const.append(res + len(taken))
  stars -= taken

const.sort(reverse=True)

print(reduce(lambda a, b: a*b, const[:3]))
