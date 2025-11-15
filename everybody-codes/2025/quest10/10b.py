import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append((0, *start))
    eaten = set()
    seen = set()
    while q:
        moves, x, y = q.popleft()
        if grid[y][x] != "#" and (y-moves >= 0 and grid[y-moves][x] == "S"):
            eaten.add((x, y-moves))
        if grid[y][x] != "#" and (y-moves+1 >= 0 and grid[y-moves+1][x] == "S"):
            eaten.add((x, y-moves+1))
        if (moves, x, y) in seen: continue
        seen.add((moves, x, y))
        if moves >= 20: continue
        for dx, dy in [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < COLS): continue
            if not (0 <= ny < ROWS): continue
            q.append((moves+1, nx, ny))
    return eaten

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "D":
            dragon = x, y
print(len(bfs(dragon)))


