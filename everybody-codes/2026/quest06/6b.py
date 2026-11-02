import sys
from collections import defaultdict, deque

lines = sys.stdin.readlines()

recipes = {}
revrec = defaultdict(set)
for line in lines:
    what, ingrs = line.strip().split(":")
    ingrs = ingrs.split(",")
    recipes[what] = set(ingrs)
    for i in ingrs:
        revrec[i].add(what)

queue = deque()
queue.append("NULL")
res = set()
seen = set()
while queue:
    cur = queue.popleft()
    if cur not in revrec or cur in seen:
        continue
    seen.add(cur)
    for i in revrec[cur]:
        queue.append(i)
        res.add(i)

res.discard("NULL")
print(len(res))
