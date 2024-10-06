from collections import defaultdict

n, k = [int(n) for n in input().split()]
graph = defaultdict(set)
nodes = set(range(1, n+1))

for _ in range(n-1):
  f, t = [int(n) for n in input().split()]
  graph[t].add(f)
  graph[f].add(t)

v = set([int(n) for n in input().split()])
assert k == len(v)

if k == 1:
  print(1)
  exit()

leafs = set()
for a in nodes:
  if len(graph[a]) == 1:
    leafs.add(a)

while leafs:
  cur = leafs.pop()

  if cur in v:
    continue

  nodes.discard(cur)

  parent = graph[cur].pop()
  graph[parent].remove(cur)
  if len(graph[parent]) == 1:
    leafs.add(parent)

print(len(nodes))
