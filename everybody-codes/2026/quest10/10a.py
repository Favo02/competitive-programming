import sys
from collections import defaultdict

grid = list(map(list, map(str.strip, sys.stdin.readlines())))
ghosts = defaultdict(list)
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell not in "#.":
            ghosts[(x, y)].append(cell)

dirs = {
    ">": (1, 0),
    "v": (0, +1),
    "<": (-1, 0),
    "^": (0, -1),
}
keys = list(dirs.keys())

collisions = 0
for round in range(10):
    nghosts = defaultdict(list)
    for (x, y), d in ghosts.items():
        for dd in d:
            dx, dy = dirs[dd]
            nx, ny = x + dx, y + dy
            if grid[ny][nx] == "#":
                nghosts[(x, y)].append(keys[(keys.index(dd) + 1) % 4])
                collisions += 1
            else:
                nghosts[(nx, ny)].append(dd)

    # print(nghosts)
    for (x, y), ds in nghosts.items():
        if len(ds) == 1:
            continue
        collisions += len(ds)
        # print(keys)
        ds = [keys[(keys.index(k) + 2) % 4] for k in ds]
        nghosts[(x, y)] = ds

    ghosts = nghosts

print(collisions)
