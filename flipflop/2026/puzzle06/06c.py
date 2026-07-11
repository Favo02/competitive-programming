import sys
from collections import deque
from math import sqrt

grid = list(map(str.strip, sys.stdin.readlines()))
grid = list(map(list, grid))

def checkprime(x, y):
    queue = deque()
    queue.append((x, y))
    seen = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        if grid[y][x] in ["#", "3"]:
            seen.add((x, y))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(grid[0])):
                continue
            if not (0 <= ny < len(grid)):
                continue
            if grid[ny][nx] in ["#", "3"]:
                queue.append((nx, ny))

    return len([i for i in range(2, int(sqrt(len(seen)))+2) if len(seen) % i == 0]) != 0

outputs = {}
banned = set()
start = None
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "S":
            start = (x, y)
        elif "A" <= cell <= "Z":
            if not checkprime(x, y):
                banned.add(cell)
            outputs[cell] = (x, y)
        elif "a" <= cell <= "z":
            pass
        elif cell in ["#", "3", "*"]:
            pass
        else:
            grid[y][x] = "_"

lights = []

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
            if grid[ny][nx].upper() in banned:
                continue
            queue.append((*outputs[grid[ny][nx].upper()], dir))

        if grid[ny][nx] in ["3", "#"]:
            # grid[ny][nx] = "L" if dir == "R" else "R"
            queue.append((nx, ny, "L" if dir == "R" else "R"))


lights.sort(key=lambda l: (l[1], l[0]))
print(lights)
print(int("".join(map(lambda l: "0" if l[2] == "L" else "1", lights)), 2))
