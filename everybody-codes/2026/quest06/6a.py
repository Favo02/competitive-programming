import sys
from collections import deque

lines = sys.stdin.readlines()

recipes = {}
for line in lines:
    what, ingrs = line.strip().split(":")
    ingrs = ingrs.split(",")
    recipes[what] = set(ingrs)

queue = deque()
queue.append("NULL")
res = set()
seen = set()
while queue:
    cur = queue.popleft()
    if cur not in recipes or cur in seen:
        continue
    seen.add(cur)
    for i in recipes[cur]:
        queue.append(i)
        res.add(i)


res.discard("NULL")
print(len(res))
