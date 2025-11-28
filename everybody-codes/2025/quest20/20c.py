import sys
from collections import defaultdict, deque

lines = list(map(lambda l: l.strip().replace(".", ""), sys.stdin.readlines()))

graph = defaultdict(list)

res = 0
start = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        graph[(x, y)].append((x, y))
        if cell == "S":
            start = x, y
        if x != len(line)-1:
            graph[(x, y)].append((x+1, y))
            graph[(x+1, y)].append((x, y))
        if y != len(lines)-1 and x % 2 == 1:
            graph[(x, y)].append((x-1, y+1))
            graph[(x-1, y+1)].append((x, y))

def rotate(grid):
    newgrid = []
    for x in range(len(grid)):
        row = []
        for y in range(len(grid)):
            if 2*x < len(grid[y]):
                row.append(grid[y][2*x])
            if 2*x+1 < len(grid[y]):
                row.append(grid[y][2*x+1])
        newgrid.append("".join(reversed(row)))
    return newgrid

grids = [lines, rotate(lines), rotate(rotate(lines))]

def bfs():
    q = deque()
    q.append((0, *start))
    seen = set()
    seen.add(start)
    while q:
        d, x, y = q.popleft()
        for ax, ay in graph[(x, y)]:
            if grids[(d+1) % 3][ay][ax] == "E":
                return d+1
            if grids[(d+1) % 3][ay][ax] != "T":
                continue
            if ((d+1) % 3, ax, ay) in seen:
                continue
            seen.add(((d+1)%3, ax, ay))
            q.append((d+1, ax, ay))
    return -1

print(bfs())
