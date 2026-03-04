import sys
from collections import deque, defaultdict

grid = list(map(list, sys.stdin.read().strip().split("\n")))
sparse = defaultdict(lambda: ".")
lim_xl = 0
lim_xr = len(grid[0])
lim_yt = 0
lim_yb = len(grid)

start = None
ends = set()
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell == "@":
            sparse[(x, y)] = cell
            start = (x, y)
        if cell == "#":
            sparse[(x, y)] = cell
            ends.add((x, y))

DIRS = [(0, -1),(0, -1),(0, -1),(1, 0),(1, 0),(1, 0),(0, +1),(0, +1),(0, +1),(-1, 0),(-1, 0),(-1, 0)]

def pprint():
    lasty = 0
    for y in range(lim_yt, lim_yb+1):
        for x in range(lim_xl, lim_xr+1):
            if y != lasty:
                lasty = y
                print()
            print(sparse[(x, y)], end="")
    print()

cached = set()
def is_surround(x, y):
    if sparse[(x, y)] == "@":
        return True
    if (x, y) in cached:
        return True

    queue = deque()
    queue.append((x, y))
    seen = set()
    while queue:
        xx, yy = queue.popleft()
        if (xx, yy) in seen:
            continue
        seen.add((xx, yy))
        for (dx, dy) in DIRS:
            nx, ny = xx+dx, yy+dy
            if not (lim_xl < nx < lim_xr): return False
            if not (lim_yt < ny < lim_yb): return False
            if sparse[(nx, ny)] in ["@", "#"]: continue
            queue.append((nx, ny))
    cached.add((x, y))
    return True

x, y = start
dir = 0
step = 0
while not all(is_surround(*e) for e in ends):
    # print(step)
    # pprint()
    dx, dy = DIRS[dir]
    dir = (dir + 1) % len(DIRS)
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
