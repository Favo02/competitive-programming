import sys
from collections import deque

lines = sys.stdin.readlines()
start = tuple(map(int, lines[0].strip().split("=")[1][1:-1].split(",")))
beacons = {
    line.strip().split("=")[0]: tuple(
        map(int, line.strip().split("=")[1][1:-1].split(","))
    )
    for line in lines[1:]
}

queue = deque()
seen = set()

queue.append(start)
seen.add(start)

while queue:
    x, y = queue.popleft()
    for bx, by in beacons.values():
        nx, ny = (x + bx) // 2, (y + by) // 2
        if (nx, ny) in seen:
            continue
        seen.add((nx, ny))
        queue.append((nx, ny))

fs = set()
for sx, sy in seen:
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        fs.add((sx + dx, sy + dy))
print(len(fs - seen))
