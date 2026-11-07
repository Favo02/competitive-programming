import sys
from collections import defaultdict

grid = [l.strip() for l in sys.stdin if l.strip()]
dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
keys = list(dirs)
LIMIT = 1000000000000

# id: (x, y, d, coll)
ghosts = {}
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in dirs:
            ghosts[len(ghosts)] = (x, y, c, 0)


def step(ghosts):
    nextt = {}
    for i, (x, y, d, c) in ghosts.items():
        dx, dy = dirs[d]
        if grid[y + dy][x + dx] == "#":
            if c + 1 >= LIMIT:
                continue
            nextt[i] = (x, y, keys[(keys.index(d) + 1) % 4], c + 1)
        else:
            nextt[i] = (x + dx, y + dy, d, c)
    cells = defaultdict(list)
    for i, (x, y, d, c) in nextt.items():
        cells[(x, y)].append(i)
    for ids in cells.values():
        if len(ids) > 1:
            for i in ids:
                x, y, d, c = nextt[i]
                if c + 1 >= LIMIT:
                    del nextt[i]
                else:
                    nextt[i] = (x, y, keys[(keys.index(d) + 2) % 4], c + 1)
    return nextt


round = 0
seen = {}
while ghosts:
    key = tuple(sorted((i, x, y, d) for i, (x, y, d, c) in ghosts.items()))
    if key in seen:
        prnd, pG = seen[key]
        loop = round - prnd
        k = min(
            [
                (LIMIT - 1 - ghosts[i][3]) // (ghosts[i][3] - pG[i][3])
                for i in ghosts
                if ghosts[i][3] > pG[i][3]
            ]
            or [0]
        )
        if k > 0:
            ghosts = {
                i: (x, y, d, c + k * (c - pG[i][3]))
                for i, (x, y, d, c) in ghosts.items()
            }
            round += k * loop
        seen = {}
    seen[key] = (round, ghosts)
    n = len(ghosts)
    ghosts = step(ghosts)
    round += 1
    if len(ghosts) != n:
        # print(round, len(ghosts))
        seen = {}
print(round)
