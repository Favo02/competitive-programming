import sys

grid = list(map(str.strip, sys.stdin.readlines()))
ROWS, COLS = len(grid), len(grid[0])

def step(grid):
    newgrid = [["_"] * COLS for _ in range(ROWS)]
    active = 0
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
    return newgrid, active

res = 0
for _ in range(10): # for part 1
# for _ in range(2025): # for part 2
    grid, a = step(grid)
    res += a

print(res)
