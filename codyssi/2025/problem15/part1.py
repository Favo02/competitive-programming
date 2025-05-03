import sys
from collections import defaultdict, deque

def place(root, node):
  left, right = tree[root]
  if node > root:
    if right:
      place(right, node)
    else:
      tree[root] = (left, node)
  else:
    if left:
      place(left, node)
    else:
      tree[root] = (node, right)

def bfs(root):
  queue = deque()
  queue.append((root, 0))
  layers = defaultdict(list)
  while queue:
    cur, depth = queue.popleft()
    layers[depth].append(cur)
    left, right = tree[cur]
    if left: queue.append((left, depth+1))
    if right: queue.append((right, depth+1))
  return layers

items, last = sys.stdin.read().strip().split("\n\n")

tree = defaultdict(lambda: (None, None))

for i, item in enumerate(items.splitlines()):
  tokens = item.split()
  id = int(tokens[2])
  if i == 0:
    tree[id] = (None, None)
    root = id
  else:
    place(root, id)

layers = [sum(v) for v in bfs(root).values()]
print(max(layers) * len(layers))
