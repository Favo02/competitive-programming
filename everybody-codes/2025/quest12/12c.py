import sys
from collections import deque

def bfs(start, seen):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        seen.add((x, y))
        for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < COLS): continue
            if not (0 <= ny < ROWS): continue
            if int(grid[y][x]) >= int(grid[ny][nx]):
                if (nx, ny) in seen: continue
                seen.add((nx, ny))
                q.append((nx, ny))
    return seen

def best(seen):
    best = 0, 0
    bestval = set()
    for ax in range(COLS):
        for ay in range(ROWS):
            newseen = bfs((ax, ay), seen.copy())
            if len(newseen) > len(bestval):
                bestval = newseen
                best = (ax, ay)
    return best, bestval

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])

(ax, ay), sa = best(set())
(bx, by), sb = best(sa)
(cx, cy), sc = best(sb)

print(len(sc))
