import sys

grid = sys.stdin.read().strip().splitlines()
grid = [list(map(int, line.split())) for line in grid]

rows = [sum(line) for line in grid]
cols = [sum(line[i] for line in grid) for i in range(len(grid[0]))]

print(min(min(rows), min(cols)))
