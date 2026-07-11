import sys
from collections import deque

grid = list(map(str.strip, sys.stdin.readlines()))
grid = list(map(list, grid))

outputs = {}
start = None
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "S":
            start = (x, y)
        elif "A" <= cell <= "Z":
            outputs[cell] = (x, y)
        elif "a" <= cell <= "z":
            pass
        elif cell in ["#", "3", "*"]:
            pass
        else:
            grid[y][x] = "_"

lights = []

# for l in grid:
#     print("".join(l))

seen = set()
queue = deque()
queue.append((*start, "L"))
while queue:
    x, y, dir = queue.popleft()
    if (x, y) in seen:
        continue
    seen.add((x, y))

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < len(grid[0])):
            continue
        if not (0 <= ny < len(grid)):
            continue

        if grid[ny][nx] == "*" and grid[y][x] in ["3", "#"]:
            lights.append((nx, ny, dir))

        if "a" <= grid[ny][nx] <= "z":
            queue.append((*outputs[grid[ny][nx].upper()], dir))

        if grid[ny][nx] in ["3", "#"]:
            # grid[ny][nx] = "L" if dir == "R" else "R"
            queue.append((nx, ny, "L" if dir == "R" else "R"))


lights.sort(key=lambda l: (l[1], l[0]))
print(lights)
print(int("".join(map(lambda l: "0" if l[2] == "L" else "1", lights)), 2))
