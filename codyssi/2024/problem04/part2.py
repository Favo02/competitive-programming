import sys
from collections import deque, defaultdict

def bfs(start, limit):

  queue = deque()
  queue.append((start, 0))
  seen = set()

  while queue:
    cur, dist = queue.popleft()
    if dist >= limit:
      continue
    for ad in graph[cur]:
      if ad in seen:
        continue
      seen.add(ad)
      queue.append((ad, dist+1))

  return seen

graph = defaultdict(list)
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  a, b = l.split(" <-> ")
  graph[a].append(b)
  graph[b].append(a)


print(len(bfs("STT", 3)))
