import sys
from collections import deque

grid = sys.stdin.readlines()
grid = list(map(list, map(str.strip, grid)))

ROWS = len(grid)
COLS = len(grid[0])


def pprint():
    for line in grid:
        print("".join(line))


def check(x, y):
    count = 0
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        if dx == dy == 0:
            continue
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] in ["#", "1"]:
            count += 1
    return count >= 5


queue = deque()
queue.append((COLS // 2, ROWS // 2))
grid[ROWS // 2][COLS // 2] = "#"
while queue:
    x, y = queue.popleft()
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] == "#":
            continue
        if check(nx, ny):
            queue.append((nx, ny))
            grid[ny][nx] = "#"

# pprint()

ans = 0
for row in grid:
    for cell in row:
        if cell == "#":
            ans += 1
print(ans)
