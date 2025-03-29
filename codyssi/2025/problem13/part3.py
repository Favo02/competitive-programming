import sys

def dfs(start, cur, visited, length):
  global res
  for adj, cost in graph[cur]:
    if adj == start:
      res = max(res, length + cost)
      continue
    if adj in visited:
      continue
    dfs(start, adj, visited | {cur}, length+cost)

lines = sys.stdin.read().strip().splitlines()
graph = {}
res = 0

for line in lines:
  tokens = line.split()
  fromm, to, cost = tokens[0], tokens[2], tokens[4]
  if fromm not in graph: graph[fromm] = []
  if to not in graph: graph[to] = []
  graph[fromm].append((to, int(cost)))

for start in graph:
  dfs(start, start, {start}, 0)

print(res)
