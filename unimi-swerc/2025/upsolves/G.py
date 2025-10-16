from collections import defaultdict
from heapq import heappop, heappush

ROWS, COLS = map(int, input().split())
sy, sx = map(lambda n: int(n)-1, input().split())
py, px = map(lambda n: int(n)-1, input().split())

grid = []
for _ in range(ROWS):
    grid.append(input().strip())
    assert len(grid[-1]) == COLS

assert grid[py][px] == "."
assert grid[sy][sx] == "."

def dijkstra(start, target):
    queue = [(0, *start)]
    dists = defaultdict(lambda: float("inf"))
    dists[start] = 0
    while queue:
        d, x, y = heappop(queue)
        if (x, y) == target: return d
        if dists[(x, y)] != d: continue
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                nx, ny = x + dx, y + dy
                if not (0 <= ny < ROWS): continue
                if not (0 <= nx < COLS): continue
                if grid[ny][nx] == '#': continue
                newd = d + ((abs(dx) + abs(dy)) > 1)
                if newd >= dists[(nx, ny)]: continue
                heappush(queue, (newd, nx, ny))
                dists[(nx, ny)] = newd
    return -1

print(dijkstra((sx, sy), (px, py)))
