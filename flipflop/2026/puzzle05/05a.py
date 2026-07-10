import sys

grid = list(map(str.strip, sys.stdin.readlines()))

seen = {(0, 0)}
x = y = 0
dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
while True:
    dx, dy = dirs[grid[y][x]]
    x += dx
    y += dy
    if (x, y) in seen: break
    seen.add((x, y))

print(len(seen))

