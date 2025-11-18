import sys
from collections import deque

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])

q = deque()
q.append((0, 0))
q.append((COLS-1, ROWS-1))
seen = set()
seen.add((0, 0))

while q:
    x, y = q.popleft()
    for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS): continue
        if not (0 <= ny < ROWS): continue
        if int(grid[y][x]) >= int(grid[ny][nx]):
            if (nx, ny) in seen: continue
            seen.add((nx, ny))
            q.append((nx, ny))

print(len(seen))
