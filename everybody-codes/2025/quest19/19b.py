import sys
from collections import deque, defaultdict

lines = [list(map(int, line.split(","))) for line in sys.stdin.readlines()]

walls = defaultdict(list)
for x, a, b in lines:
    walls[x].append((a, a+b))

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
        valid = False
        for a, b in walls[x]:
            if (a <= y < b):
                valid = True
        if not valid:
            continue

    if x >= lines[-1][0]:
        res = min(res, t)
        continue

    q.append((x+1, y+1, t+1))
    q.append((x+1, y-1, t))

print(res)
