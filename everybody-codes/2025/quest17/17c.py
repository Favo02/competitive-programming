import sys
from heapq import heappop, heappush

lines = list(map(str.strip, sys.stdin.readlines()))

Xv = Yv = None
Xs = Ys = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == "@":
            Xv, Yv = x, y
        if cell == "S":
            Xs, Ys = x, y

ROWS, COLS = len(lines), len(lines[0])

lines[Ys] = lines[Ys].replace("S", "0")

def dijkstra():
    q = [(0, (Xs, Ys), False, (Xv - Xs)**2 + (Yv - Ys)**2)]
    dists = {}

    while q:
        time, (x, y), pivoted, closest = heappop(q)
        if (x, y) == (Xs, Ys) and pivoted:
            return time

        key = ((x, y), pivoted, closest)
        if key in dists and dists[key] <= time:
            continue
        dists[key] = time

        radius = time // 30
        if closest <= radius**2:
            continue

        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+dx, y+dy
            if not (0 <= ny < ROWS): continue
            if pivoted:
                if not (Xv-2 <= nx < COLS): continue
            else:
                if not (0 <= nx <= Xv+2): continue

            newdist = (Xv - nx)**2 + (Yv - ny)**2
            if newdist <= radius**2:
                continue
            newclosest = min(closest, newdist)
            newtime = time + int(lines[ny][nx])
            heappush(q, (newtime, (nx, ny), pivoted or nx == Xv and ny > Yv, newclosest))
    return -1

d = dijkstra()
print(d * (d // 30))
