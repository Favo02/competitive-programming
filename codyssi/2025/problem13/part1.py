import sys
from collections import defaultdict, deque
from functools import reduce

def bfs(start):
  queue = deque()
  queue.append(start)
  dist = {start: 0}
  while queue:
    cur = queue.popleft()
    for adj, _ in graph[cur]:
      if adj in dist:
        continue
      queue.append(adj)
      dist[adj] = dist[cur] + 1
  return dist

lines = sys.stdin.read().strip().splitlines()
graph = defaultdict(list)

for line in lines:
  tokens = line.split()
  fromm, to, cost = tokens[0], tokens[2], tokens[4]
  graph[fromm].append((to, int(cost)))

print(reduce(lambda a, b: a * b, sorted(bfs("STT").values(), reverse=True)[:3], 1))
