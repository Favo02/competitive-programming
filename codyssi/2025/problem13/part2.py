import sys
import heapq
from collections import defaultdict
from functools import reduce

def dijkstra(start):
  queue = []
  queue.append((0, start))
  dist = defaultdict(lambda: float("inf"))
  dist[start] = 0
  while queue:
    d, cur = heapq.heappop(queue)
    assert dist[cur] == d
    for adj, cost in graph[cur]:
      if dist[cur] + cost < dist[adj]:
        heapq.heappush(queue, (dist[cur] + cost, adj))
        dist[adj] = dist[cur] + cost
  return dist

lines = sys.stdin.read().strip().splitlines()
graph = defaultdict(list)

for line in lines:
  tokens = line.split()
  fromm, to, cost = tokens[0], tokens[2], tokens[4]
  graph[fromm].append((to, int(cost)))

print(reduce(lambda a, b: a * b, sorted(dijkstra("STT").values(), reverse=True)[:3], 1))
