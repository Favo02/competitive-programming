import sys

grid = list(map(lambda l: list(l.strip()), sys.stdin.readlines()))
ROWS = len(grid)
COLS = len(grid[0])
DIRS = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}

def calc(cx, cy, nd):
    od = grid[cy][cx]
    grid[cy][cx] = nd
    errors = 0
    seen = {(0, 0)}
    x = y = 0
    while True:
        dx, dy = DIRS[grid[y][x]]
        x += dx
        y += dy
        stop = False
        while (x, y) in seen:
            if errors == 3:
                stop = True
                break
            errors += 1
            if not (1 <= y < ROWS-1):
                stop = True
                break
            if not (1 <= x < COLS-1):
                stop = True
                break
            turn = TURN[grid[y][x]]
            dx, dy = DIRS[turn]
            x += dx
            y += dy
        seen.add((x, y))
        if stop:
            break

    grid[cy][cx] = od
    return len(seen)

res = 0
for y in range(1, ROWS-1):
    for x in range(1, COLS-1):
        for nd in DIRS.keys():
            res = max(res, calc(x, y, nd))
print(res)
