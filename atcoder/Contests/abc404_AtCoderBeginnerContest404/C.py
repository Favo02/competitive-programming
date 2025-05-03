from collections import deque

def bfs(start):
  queue = deque()
  queue.append(start)
  seen = set()
  while queue:
    cur = queue.popleft()
    if cur in seen:
      continue
    seen.add(cur)
    for ad in graph[cur]:
      queue.append(ad)
  return seen

N, M = map(int, input().split())

edges = []
degree = [0] * N
graph = [[] for _ in range(N)]

for _ in range(M):
  f, t = map(int, input().split())
  graph[f-1].append(t-1)
  graph[t-1].append(f-1)
  degree[f-1] += 1
  degree[t-1] += 1
  edges.append((f, t))

if N != M: print("No")
elif all(d == 2 for d in degree) and len(bfs(0)) == N: print("Yes")
else: print("No")
