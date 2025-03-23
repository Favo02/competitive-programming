import sys
from collections import deque, defaultdict

def bfs(start):

  queue = deque()
  queue.append((start, 0))
  seen = set()
  seen.add(start)
  res = 0

  while queue:
    cur, dist = queue.popleft()
    res += dist
    for ad in graph[cur]:
      if ad in seen:
        continue
      seen.add(ad)
      queue.append((ad, dist+1))

  return res

graph = defaultdict(list)
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  a, b = l.split(" <-> ")
  graph[a].append(b)
  graph[b].append(a)

print(bfs("STT"))
