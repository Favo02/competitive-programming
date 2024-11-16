from collections import defaultdict
import sys

def dfs(dist, path, cur):
  if cur == "@":
    fruits.append((dist, path + "@"))
    return
  if cur not in tree:
    return
  for adj in tree[cur]:
    dfs(dist+1, path + cur[0], adj)

tree = {}

for line in sys.stdin:
  fr, too = line.strip().split(":")
  to = filter(lambda t: t != "ANT" and t != "BUG", too.split(","))
  tree[fr] = to

fruits = []
dfs(0, "", "RR")

count = defaultdict(int)
for l, f in fruits:
  count[l] += 1

for l, f in fruits:
  if count[l] == 1:
    print(f)
