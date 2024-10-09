from collections import deque

pup, fri = map(int, input().split())

graph = [[] for _ in range(pup)]
for _ in range(fri):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

NOT = {1: 2, 2: 1}

res = [-1] * pup

def bfs(start):
  queue = deque([start])

  while queue:
    cur = queue.pop()

    for adj in graph[cur]:
      if res[adj] == -1:
        res[adj] = NOT[res[cur]]
        queue.append(adj)
      elif res[adj] == res[cur]:
        return False

  return True

for p in range(pup):
  if res[p] == -1:
    res[p] = 1
    valid = bfs(p)
    if not valid:
      print("IMPOSSIBLE")
      break
else:
  for r in res:
    print(r, end=" ")
  print()
