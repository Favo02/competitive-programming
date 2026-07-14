from collections import deque
import sys
grid = list(map(str.strip, sys.stdin.readlines()))

start = None
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x, y)

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
            if not (0 <= nx < len(grid[0])): continue
            if not (0 <= ny < len(grid)): continue
            if grid[ny][nx] == "#": continue
            if grid[ny][nx] == "E": return d+1
            queue.append((nx, ny, d+1))

print(bfs())
