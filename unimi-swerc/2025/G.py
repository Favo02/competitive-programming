from collections import deque, defaultdict

ROWS, COLS = map(int, input().split())
sy, sx = map(lambda n: int(n)-1, input().split())
py, px = map(lambda n: int(n)-1, input().split())

grid = []
for _ in range(ROWS):
    grid.append(input().strip())
    assert len(grid[-1]) == COLS

# print(grid)

assert grid[py][px] == "."
assert grid[sy][sx] == "."

def bfs(queue):
    global seen
    jump = set()
    while queue:
        x, y = queue.popleft()
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < ROWS): continue
                if not (0 <= ny < COLS): continue
                if grid[ny][nx] == '#': continue
                if (nx, ny) in seen: continue
                if abs(dx) + abs(dy) <= 1:
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                else:
                    jump.add((nx, ny))
    return seen, jump-seen

dist = 0
cur = [(sx, sy)]
seen = set()
while True:
    s, j = bfs(deque(deque(cur)))
    if (px, py) in s:
        print(dist)
        break
    if not s or not j:
        print(-1)
        break
    dist += 1
    cur = list(j)
