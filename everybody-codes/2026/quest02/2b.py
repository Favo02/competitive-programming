import sys
from collections import defaultdict
from operator import itemgetter

lines = sys.stdin.readlines()

ans = 0

for line in lines:
    line = line.strip()
    tokens = line.split()
    greather = [0] * 9

    bigger = defaultdict(list)
    for t in tokens:
        a = int(t[0]) - 1
        b = int(t[2]) - 1
        if t[1] == ">":
            bigger[a].append(b)
            greather[a] += 1
        else:
            bigger[b].append(a)
            greather[b] += 1

    def tie():
        for i, a in enumerate(greather):
            for ii, b in enumerate(greather):
                if i == ii:
                    continue
                if a == b:
                    if ii in bigger[i]:
                        greather[i] += 1
                    else:
                        greather[ii] += 1
                    return

    tie()
    res = list(enumerate(greather))
    res.sort(key=itemgetter(1), reverse=True)
    res = int("".join([str(t[0] + 1) for t in res]))
    ans += res

print(ans)
