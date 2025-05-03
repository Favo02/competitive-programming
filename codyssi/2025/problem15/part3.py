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

def search(root, node):
  if not root:
    return []
  if node > root:
    return [root] + search(tree[root][1], node)
  else:
    return [root] + search(tree[root][0], node)

items, last = sys.stdin.read().strip().split("\n\n")
names = {}

tree = defaultdict(lambda: (None, None))
for i, item in enumerate(items.splitlines()):
  tokens = item.split()
  id = int(tokens[2])
  names[id] = tokens[0]
  if i == 0:
    tree[id] = (None, None)
    root = id
  else:
    place(root, id)

common = set()
for item in last.splitlines():
  tokens = item.split()
  id = int(tokens[2])
  if not common:
    common = set(search(root, id))
  else:
    common = common.intersection(set(search(root, id)))

# hack: use the fact that sets are ordered using insertion time
print(names[list(common)[-1]])
