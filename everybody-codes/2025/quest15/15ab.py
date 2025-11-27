from collections import deque

instr = input().split(",")

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

cur = 3
x = y = 0

path = set()
path.add((0, 0))

for ins in instr:
    d, qty = ins[0], int(ins[1:])
    cur = (cur + 1 if d == "R" else cur - 1) % 4
    for _ in range(qty):
        x += DIRS[cur][0]
        y += DIRS[cur][1]
        path.add((x, y))

maxx = max(x for x, y in path)
minx = min(x for x, y in path)
maxy = max(y for x, y in path)
miny = min(y for x, y in path)

def bfs(start):
    q = deque()
    q.append((*start, 0))
    seen = set()
    seen.add(start)
    while q:
        x, y, d = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x+dx, y+dy
            if not (minx - 5 < nx < maxx + 5):
                continue
            if not (miny - 5 < ny < maxy + 5):
                continue
            if (nx, ny) in seen:
                continue
            if (nx, ny) == (0,0):
                return d+1
            if (nx, ny) in path:
                continue
            q.append((nx, ny, d+1))
            seen.add((nx, ny))

print(bfs((x, y)))
