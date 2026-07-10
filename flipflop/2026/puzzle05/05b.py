import sys

grid = list(map(lambda l: list(l.strip()), sys.stdin.readlines()))
ROWS = len(grid)
COLS = len(grid[0])
DIRS = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}

def calc(cx, cy, nd):
    od = grid[cy][cx]
    grid[cy][cx] = nd

    seen = {(0, 0)}
    x = y = 0
    while True:
        dx, dy = DIRS[grid[y][x]]
        x += dx
        y += dy
        if (x, y) in seen: break
        seen.add((x, y))

    grid[cy][cx] = od
    return len(seen)

res = 0
for y in range(1, ROWS-1):
    for x in range(1, COLS-1):
        for nd in DIRS.keys():
            res = max(res, calc(x, y, nd))
print(res)
