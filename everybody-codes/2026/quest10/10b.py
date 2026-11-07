import sys
from collections import defaultdict

grid = list(map(list, map(str.strip, sys.stdin.readlines())))
ghosts = defaultdict(list)
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell not in "#.":
            ghosts[(x, y)].append((cell, 0))

dirs = {
    ">": (1, 0),
    "v": (0, +1),
    "<": (-1, 0),
    "^": (0, -1),
}
keys = list(dirs.keys())
LIMIT = 10
LIMIT = 10000

round = 0
while len(ghosts) > 0:
    nghosts = defaultdict(list)
    for (x, y), d in ghosts.items():
        for dd, coll in d:
            dx, dy = dirs[dd]
            nx, ny = x + dx, y + dy
            if grid[ny][nx] == "#":
                if coll + 1 >= LIMIT:
                    continue
                nghosts[(x, y)].append((keys[(keys.index(dd) + 1) % 4], coll + 1))
            else:
                nghosts[(nx, ny)].append((dd, coll))

    for (x, y), ds in nghosts.items():
        if len(ds) == 1:
            continue
        ds = [(keys[(keys.index(k) + 2) % 4], c + 1) for (k, c) in ds if c + 1 < LIMIT]
        if len(ds) > 0:
            nghosts[(x, y)] = ds
        # else:
        # nghosts.pop((x, y))

    ghosts = nghosts
    round += 1
print(round)
