from collections import deque

def bfs(start, end):

  queue = deque([start])
  seen = set([start])
  prec = [-1] * nodes

  while queue:
    cur = queue.popleft()
    for adj in graph[cur]:
      if adj in seen: continue
      seen.add(adj)
      queue.append(adj)
      prec[adj] = cur
      if adj == end:
        break

  return prec

def path(start, end, prec):
  cur = end
  path = [ end ]
  while cur != start:
    path.append(prec[cur])
    cur = prec[cur]
  return list(reversed(path))

nodes, edges = map(int, input().split())

graph = {n: [] for n in range(nodes)}
for _ in range(edges):
  f, t = map(int, input().split())
  graph[f-1].append(t-1)
  graph[t-1].append(f-1)

prec = bfs(0, nodes-1)
if prec[nodes-1] == -1:
  print("IMPOSSIBLE")
else:
  p = path(0, nodes-1, prec)
  print(len(p))
  for n in p:
    print(n+1, end=" ")
  print()
