import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append((0, *start))
    seen = set()
    eaten = set()
    while q:
        moves, x, y = q.popleft()
        if grid[y][x] == "S":
            eaten.add((x, y))
        if (x, y) in seen: continue
        seen.add((x, y))
        if moves >= 4: continue
        for dx, dy in [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < COLS): continue
            if not (0 <= ny < ROWS): continue
            q.append((moves+1, nx, ny))
    return seen, eaten

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "D":
            dragon = x, y
print(len(bfs(dragon)[1]))


