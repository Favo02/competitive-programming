from collections import deque
# from collections import Counter
# from collections import defaultdict
# import heapq
# import bisect
# from functools import lru_cache
# import math

# import sys
# sys.setrecursionlimit(10**5)

def bfs(starts):
  queue = deque([(0, x, y) for x, y in starts])

  seen = {(x, y) for x, y in starts}

  while queue:
    cur = queue.popleft()
    d, x, y = cur

    if d == dist: continue

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
      nx, ny = x + dx, y + dy
      # print(nx, ny)
      if not (0 <= nx < C): continue
      if not (0 <= ny < R): continue
      if (nx, ny) in seen: continue
      if field[ny][nx] == "#": continue

      seen.add((nx, ny))
      queue.append((d+1, nx, ny))

  return seen


R, C, dist = map(int, input().split())

field = []
starts = set()
for r in range(R):
  field.append(input())
  for c, cell in enumerate(field[-1]):
    if cell == "H":
      starts.add((c, r))

hum = bfs(starts)
print(len(hum))
