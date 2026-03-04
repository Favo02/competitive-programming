import sys

grid = list(map(list, sys.stdin.read().split("\n")))

start = end = None
for y, line in enumerate(grid):
    if "#" in line:
        end = (line.index("#"), y)
    if "@" in line:
        start = (line.index("@"), y)

DIRS = [(0, -1), (1, 0), (0, +1), (-1, 0)]

def pprint():
    for l in grid:
        print(l)

x, y = start
dir = 0
step = 0
while True:
    dx, dy = DIRS[dir % 4]
    dir = (dir + 1) % 4
    if grid[y + dy][x + dx] == '#':
        print(step+1)
        break
    if grid[y + dy][x + dx] == '@':
        continue
    grid[y + dy][x + dx] = '@'
    x += dx
    y += dy
    step += 1
