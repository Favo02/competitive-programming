import sys
from collections import deque

lines = [list(map(int, line.split(","))) for line in sys.stdin.readlines()]

walls = {x: (a, a+b) for x, a, b in lines}

q = deque()
q.append((0, 0, 0))

res = float("inf")
seen = {}

while q:
    x, y, t = q.popleft()
    if (x, y) in seen and seen[(x, y)] <= t:
        continue
    seen[(x, y)] = t

    if y < 0: continue

    if x in walls:
        a, b = walls[x]
        if not (a <= y < b):
            continue
    if x >= lines[-1][0]:
        res = min(res, t)
        continue

    q.append((x+1, y+1, t+1))
    q.append((x+1, y-1, t))

print(res)
