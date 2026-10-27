import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

start = None
N = int(input())
graph = defaultdict(list)
roads = []
for _ in range(N - 1):
    a, b, h = map(int, input().split())
    roads.append((h, a, b))
    if start is None:
        start = a
    graph[a].append((b, h))
    graph[b].append((a, h))

dsu = [i for i in range(N)]
size = [1] * N


def find(x):
    if dsu[x] != x:
        dsu[x] = find(dsu[x])
    return dsu[x]


def union(x, y):
    rx = find(x)
    ry = find(y)
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    dsu[ry] = rx
    size[rx] += size[ry]


roads.sort()
res = 0
for h, a, b in roads:
    a -= 1
    b -= 1
    ra = find(a)
    rb = find(b)
    res += h * size[ra] * size[rb]
    union(a, b)
print(res)
