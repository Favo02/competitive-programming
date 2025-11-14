import sys
from collections import defaultdict

unionfind = defaultdict(lambda: -1)

def merge(a, b):
    if get(a) == get(b):
        return
    unionfind[get(a)] = get(b)

def get(a):
    cur = a
    while unionfind[cur] != -1:
        cur = unionfind[cur]
    return cur

dnas = list(map(lambda l: l.strip().split(":")[1], sys.stdin.readlines()))

for i, p1 in enumerate(dnas):
    for ii, p2 in enumerate(dnas):
        if i <= ii: continue
        for iii, c in enumerate(dnas):
            if i == iii: continue
            if ii == iii: continue
            if all(c in [p1, p2] for p1, p2, c in zip(p1, p2, c)):
                merge(i, ii)
                merge(i, iii)

families = defaultdict(lambda: [0, 0])

for i in range(len(dnas)):
    g = get(i)
    families[g][0] += 1
    families[g][1] += i+1

print(max(families.values())[1])
