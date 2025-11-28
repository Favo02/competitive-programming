import sys
from collections import deque, defaultdict

lines = [list(map(int, line.split(","))) for line in sys.stdin.readlines()]

walls = defaultdict(list)
for x, a, b in lines:
    walls[x].append((a, a+b))

wallsX = list(walls)
wallsY = list(walls.values())

cur = {0: 0}
x = 0

for targetX, v in zip(wallsX, wallsY):
    next = {}

    for miny, maxy in v:
        for targetY in range(miny, maxy):
            for y, t in cur.items():
                dx, dy = targetX - x, abs(targetY - y)
                if dy > dx:
                    continue
                if dy % 2 != dx % 2:
                    continue

                flaps = 0
                if targetY < y:
                    flaps += (dx - dy) // 2
                else:
                    flaps += dy + (dx - dy)//2

                if targetY in next:
                    next[targetY] = min(next[targetY], t + flaps)
                else:
                    next[targetY] = t + flaps

    x = targetX
    cur = next

print(min(cur.values()))
