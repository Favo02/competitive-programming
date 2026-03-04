import sys
from collections import deque, defaultdict
from operator import itemgetter

grid = list(map(list, sys.stdin.read().strip().split("\n")))
sparse = defaultdict(lambda: ".")
lim_xl = 0
lim_xr = len(grid[0])
lim_yt = 0
lim_yb = len(grid)

start = end = None
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "@":
            sparse[(x, y)] = cell
            start = (x, y)
        if cell == "#":
            sparse[(x, y)] = cell
            end = (x, y)

DIRS = [(0, -1), (1, 0), (0, +1), (-1, 0)]

def pprint():
    lasty = 0
    for y in range(lim_yt, lim_yb+1):
        for x in range(lim_xl, lim_xr+1):
            if y != lasty:
                lasty = y
                print()
            print(sparse[(x, y)], end="")
    print()

def is_surround(x, y):
    if sparse[(x, y)] == "@":
        return True

    queue = deque()
    queue.append((x, y))
    seen = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for (dx, dy) in DIRS:
            nx, ny = x+dx, y+dy
            if not (lim_xl < nx < lim_xr): return False
            if not (lim_yt < ny < lim_yb): return False
            if sparse[(nx, ny)] in ["@", "#"]: continue
            queue.append((nx, ny))
    return True

x, y = start
dir = 0
step = 0
while not is_surround(*end):
    # pprint()
    dx, dy = DIRS[dir % 4]
    dir = (dir + 1) % 4
    nx, ny = x + dx, y + dy
    if sparse[(nx, ny)] == "#" or is_surround(nx, ny):
        continue
    sparse[(nx, ny)] = '@'
    lim_xl = min(lim_xl, nx - 5)
    lim_xr = max(lim_xr, nx + 5)
    lim_yt = min(lim_yt, ny - 5)
    lim_yb = max(lim_yb, ny + 5)
    x += dx
    y += dy
    step += 1
print(step)
