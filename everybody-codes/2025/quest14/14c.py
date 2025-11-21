import sys

pattern = list(map(str.strip, sys.stdin.readlines()))
ROWS = COLS = 34

grid = [["."] * COLS for _ in range(ROWS)]

def step(grid):
    newgrid = [["_"] * COLS for _ in range(ROWS)]
    active = 0
    special = True
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            c = 0
            for dx, dy in [(-1,1),(1,1),(1,-1),(-1,-1)]:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < COLS): continue
                if not (0 <= ny < ROWS): continue
                if grid[ny][nx] == "#":
                    c += 1
            if cell == "#" and c % 2 == 1 or cell == "." and c % 2 == 0:
                newgrid[y][x] = "#"
                active += 1
            else:
                newgrid[y][x] = "."

            if 13 <= x <= 20 and 13 <= y <= 20:
                if newgrid[y][x] != pattern[y-13][x-13]:
                    special = False

    return newgrid, active, special

seen = {}
specials = []

for i in range(1000000000):
    grid, a, spec = step(grid)

    if spec:
        specials.append((i+1, a))

    frozen_grid = tuple(tuple(line) for line in grid)
    if frozen_grid in seen:
        cycle = i - seen[frozen_grid]
        break

    seen[frozen_grid] = i

def solve():
    res = 0
    mult = 0
    while True:
        for round, active in specials:
            if (cycle * mult) + round >= 1000000000:
                return res
            res += active
        mult += 1

print(solve())
