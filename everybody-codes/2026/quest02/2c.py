import sys
from collections import defaultdict
from operator import itemgetter

lines = sys.stdin.readlines()

ans = 0

for line in lines:
    line = line.strip()
    tokens = line.split()

    bigger = defaultdict(set)
    for t in tokens:
        a = int(t[0]) - 1
        b = int(t[2]) - 1
        if t[1] == ">":
            bigger[a].add(b)
        else:
            bigger[b].add(a)

    for a in range(9):
        for b in bigger[a].copy():
            for c in bigger[b]:
                bigger[a].add(c)

    res = [(a, len(bigger[a])) for a in range(9)]
    res.sort(key=itemgetter(1), reverse=True)
    res = int("".join([str(t[0] + 1) for t in res]))
    ans += res

print(ans)
