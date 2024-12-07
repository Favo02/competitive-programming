# from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

def count(r, c):
  hum = set()
  for rr, row in enumerate(field):
    for cc, cell in enumerate(row):
      if field[rr][cc] == "#": continue
      if abs(rr - r) + abs(cc - c) <= dist:
        hum.add((rr, cc))
  return hum

R, C, dist = map(int, input().split())

field = []
poss = set()
for r in range(R):
  field.append(input())
  for c, cell in enumerate(field[-1]):
    if cell == ".":
      poss.add((r, c))

ans = 0

for r1, c1 in poss:
  for r2, c2 in poss:
    if r1 == r2 and c1 == c2: continue
    ans = max(ans, len(count(r1, c1) | count(r2, c2)))

print(ans)
