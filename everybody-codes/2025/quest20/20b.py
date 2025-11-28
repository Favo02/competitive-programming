import sys
from collections import defaultdict, deque

lines = list(map(lambda l: l.strip().replace(".", ""), sys.stdin.readlines()))

graph = defaultdict(list)

start = end = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell in "#.":
            continue
        if cell == "S":
            start = x, y
        if cell == "E":
            end = x, y
        if x != len(line)-1 and line[x+1] in "TSE":
            graph[(x, y)].append((x+1, y))
            graph[(x+1, y)].append((x, y))
        if y != len(lines)-1 and x % 2 == 1 and lines[y+1][x-1] in "TSE":
            graph[(x, y)].append((x-1, y+1))
            graph[(x-1, y+1)].append((x, y))

def bfs():
    q = deque()
    q.append((0, *start))
    seen = set()
    seen.add(start)
    while q:
        d, x, y = q.popleft()
        for ad in graph[(x, y)]:
            if ad == end:
                return d+1
            if ad in seen:
                continue
            seen.add(ad)
            q.append((d+1, *ad))
    return -1

print(bfs())
