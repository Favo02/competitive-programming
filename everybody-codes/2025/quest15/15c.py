from heapq import heappop, heappush

instr = input().split(",")

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

cur = 3
x = y = 0
lx = ly = 0

walls = []
points = set()
points.add((0, 0))

for ins in instr:
    d, qty = ins[0], int(ins[1:])
    cur = (cur + 1 if d == "R" else cur - 1) % 4

    x = lx + DIRS[cur][0] * qty
    y = ly + DIRS[cur][1] * qty
    walls.append((lx, ly, x, y))
    points.add((x, y))
    lx, ly = x, y

grid = set()
for x1, y1 in points:
    for x2, y2 in points:
        for dx, dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
            grid.add((x1+dx, y2+dy))
            grid.add((x2+dx, y1+dy))

for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
    grid.add((dx, dy))
    grid.add((lx+dx, ly+dy))

def valid(x, y, ax, ay):
    if not (ax == x or ay == y):
        return False
    for wx1, wy1, wx2, wy2 in walls:
        # vertical
        if x == ax:
            # wall vertical
            if wx1 == wx2:
                if x == wx1 and not (max(y, ay) < min(wy1, wy2) or min(y, ay) > max(wy1, wy2)):
                    return False
            # wall horizontal
            else:
                if min(wx1, wx2) <= x <= max(wx1, wx2) and min(y, ay) <= wy1 <= max(y, ay):
                    return False
        # horizontal
        else:
            # wall horizontal
            if wy1 == wy2:
                if y == wy1 and not (max(x, ax) < min(wx1, wx2) or min(x, ax) > max(wx1, wx2)):
                    return False
            # wall vertical
            else:
                if min(wy1, wy2) <= y <= max(wy1, wy2) and min(x, ax) <= wx1 <= max(x, ax):
                    return False
    return True

def dijkstra():
    q = [(0, lx-1, ly), (0, lx+1, ly), (0, lx, ly-1), (0, lx, ly+1)]
    dists = {(b, c): a for a, b, c in q}
    while q:
        d, x, y = heappop(q)
        for ax, ay in grid:
            if (ax, ay) == (x, y): continue
            if not valid(x, y, ax, ay):
                continue
            newdist = d + abs(ax - x) + abs(ay - y)
            if abs(ax) + abs(ay) <= 1:
                return newdist + 2
            if (ax, ay) in dists and dists[(ax, ay)] <= newdist:
                continue
            dists[(ax, ay)] = newdist
            heappush(q, (newdist, ax, ay))
    return -1

print(dijkstra())
