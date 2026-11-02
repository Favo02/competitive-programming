import sys
from collections import deque

lines = sys.stdin.readlines()

recipes = {}
for line in lines:
    what, ingrs = line.strip().split(":")
    ingrs = ingrs.split(",")
    recipes[what] = set(ingrs)

ans = 0
for r in recipes:
    queue = deque()
    queue.append(r)
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

    if len(res & {"NULLv1", "NULLv2", "NULLv3"}) >= 2:
        ans += 1

print(ans)
