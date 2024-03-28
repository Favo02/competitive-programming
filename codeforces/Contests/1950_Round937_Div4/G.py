from collections import deque
from itertools import combinations

def bfs(graph):
  queue = deque()
  for s in graph:
    queue.append((s, 1 << s))

  seen = set()

  while queue:
    cur, vis = queue.popleft()
    if vis == (1 << len(graph)) -1:
      return True

    for adj in graph[cur]:
      if (1 << adj) & vis != 0:
        continue
      next = (adj, vis | (1 << adj))
      if next not in seen:
        queue.append(next)
        seen.add(next)
  return False

def remove_node(graph, remove):
  ng = {}
  for node, edges in graph.items():
    if node == remove:
      continue
    ed = [e-1 if e > remove else e for e in edges if e != remove]
    if node > remove:
      ng[node-1] = ed
    elif node < remove:
      ng[node] = ed
  return ng

def remove_nodes(graph, removed):
  # ng = graph
  for r in removed:
    graph = remove_node(graph, r)
    # print(ng)
  return graph

def solve():
  # print("==========")
  songs_len = int(input())
  songs = []
  for _ in range(songs_len):
    genre, artist = input().split()
    songs.append((genre, artist))

  if songs_len == 1:
    return 0

  graph = {i: [] for i in range(songs_len)}
  for i in range(songs_len):
    for j in range(i+1, songs_len):
      if songs[i][0] == songs[j][0] or songs[i][1] == songs[j][1]:
        graph[i].append(j)
        graph[j].append(i)

  for num_to_remove in range(0, songs_len):
    for removed in combinations(range(songs_len), num_to_remove):
      removed = sorted(removed, reverse=True)
      ng = remove_nodes(graph, removed)
      res = bfs(ng)
      if res:
        return num_to_remove

cases = int(input())
for _ in range(cases):
  res = solve()
  print(res)
