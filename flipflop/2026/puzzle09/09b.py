from collections import deque, defaultdict
import sys
grid = list(map(str.strip, sys.stdin.readlines()))

start = None
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x, y)

# print("\n".join(grid))

graph = defaultdict(list)
for y, line in enumerate(grid):
    last = -1
    for x, cell in enumerate(line):
        if cell == "#":
            if last+1 < x-1:
                si = (last+1, y)
                ei = (x-1, y)
                for p in range(last+1, x):
                    if (p, y) != si: graph[(p, y)].append(si)
                    if (p, y) != ei: graph[(p, y)].append(ei)
            last = x

for x in range(len(grid[0])):
    last = -1
    for y in range(len(grid)):
        if grid[y][x] == "#":
            if last+1 < y-1:
                si = (x, last+1)
                ei = (x, y-1)
                for p in range(last+1, y):
                    if (x, p) != si: graph[(x, p)].append(si)
                    if (x, p) != ei: graph[(x, p)].append(ei)
            last = y

def bfs():
    queue = deque()
    queue.append((*start, 0))
    seen = set()
    while queue:
        x, y, d = queue.popleft()
        if (x, y) in seen: continue
        seen.add((x, y))

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x+dx, y+dy
            if grid[ny][nx] == "#": continue
            if grid[ny][nx] == "E": return d+1
            queue.append((nx, ny, d+1))
        for tx, ty in graph[(x, y)]:
            if grid[ty][tx] == "#": continue
            if grid[ty][tx] == "E": return d+1
            queue.append((tx, ty, d+1))


print(bfs())
