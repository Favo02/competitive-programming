import sys
from collections import deque

grid = sys.stdin.readlines()
grid = list(map(list, map(str.strip, grid)))

ROWS = len(grid)
COLS = len(grid[0])


def pprint():
    for line in grid:
        print("".join(line))


def check(x, y, what):
    count = 0
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        if dx == dy == 0:
            continue
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] in what:
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
        if check(nx, ny, "#1"):
            queue.append((nx, ny))
            grid[ny][nx] = "#"

# pprint()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "#":
            grid[y][x] = "."

queue = deque()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "#":
            for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < COLS):
                    queue.append((x, y))
                    grid[y][x] = "="
                    continue
                if not (0 <= ny < ROWS):
                    queue.append((x, y))
                    grid[y][x] = "="
                    continue
                if grid[ny][nx] == ".":
                    queue.append((x, y))
                    grid[y][x] = "="

# pprint()

while queue:
    x, y = queue.popleft()
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] == "=":
            continue
        if check(nx, ny, "="):
            queue.append((nx, ny))
            grid[ny][nx] = "="

pattern = (
    {(a, b) for a in range(-1, 2) for b in range(-1, 2)}
    | {(a, b) for a in range(-1, 2) for b in [-2, +2]}
    | {(a, b) for b in range(-1, 2) for a in [-2, +2]}
)

ans = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != "#":
            continue
        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < COLS):
                break
            if not (0 <= ny < ROWS):
                break
            if grid[ny][nx] not in "#@":
                break
        else:
            grid[y][x] = "@"

# pprint()


def check2(x, y):
    count = 0
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        if dx == dy == 0:
            continue
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] == "@":
            count += 1
        if grid[ny][nx] == "=":
            return False
    return count >= 4


willbe = []
for x, y in [(x, y) for x in range(COLS) for y in range(ROWS)]:
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] == "@":
            continue
        if check2(nx, ny):
            willbe.append((nx, ny))

for x, y in willbe:
    grid[y][x] = "@"

# pprint()

willbe = []
for x, y in [(x, y) for x in range(COLS) for y in range(ROWS)]:
    for dx, dy in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < COLS):
            continue
        if not (0 <= ny < ROWS):
            continue
        if grid[ny][nx] == "@":
            continue
        if check2(nx, ny):
            willbe.append((nx, ny))

for x, y in willbe:
    grid[y][x] = "@"


ans = 0
for x, y in [(x, y) for x in range(COLS) for y in range(ROWS)]:
    if grid[y][x] == "@":
        ans += 1
# pprint()

print(ans)
