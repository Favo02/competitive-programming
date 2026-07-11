import sys
from collections import deque

grid = list(map(str.strip, sys.stdin.readlines()))
grid = list(map(list, grid))

start = None
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "S":
            start = (x, y)
            grid[y][x] = "L"

lights = []

queue = deque()
queue.append(start)
while queue:
    x, y = queue.popleft()
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < len(grid[0])):
            continue
        if not (0 <= ny < len(grid)):
            continue
        if grid[ny][nx] == "*":
            lights.append((nx, ny, grid[y][x]))
        if grid[ny][nx] != "#":
            continue
        grid[ny][nx] = "L" if grid[y][x] == "R" else "R"
        queue.append((nx, ny))

for l in grid:
    print("".join(l))

lights.sort(key=lambda l: (l[1], l[0]))
print(int("".join(map(lambda l: "0" if l[2] == "L" else "1", lights)), 2))
