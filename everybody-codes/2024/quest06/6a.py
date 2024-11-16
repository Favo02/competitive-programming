from collections import defaultdict
import sys

def dfs(path, cur):
  if cur == "@":
    fruits.append((len(path), path))
    return
  for adj in tree[cur]:
    dfs(path + [ cur ], adj)

tree = defaultdict(list)

for line in sys.stdin:
  fr, too = line.strip().split(":")
  to = too.split(",")
  tree[fr].extend(to)

fruits = []
dfs([], "RR")

count = defaultdict(int)
for l, f in fruits:
  count[l] += 1

for l, f in fruits:
  if count[l] == 1:
    print("".join(f + ["@"]))
