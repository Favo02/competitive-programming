import sys
from operator import itemgetter

lines = sys.stdin.readlines()

ans = 0

for line in lines:
    line = line.strip()
    tokens = line.split()
    greather = [0] * 5
    for t in tokens:
        a = int(t[0]) - 1
        b = int(t[2]) - 1
        if t[1] == ">":
            greather[a] += 1
        else:
            greather[b] += 1
    res = list(enumerate(greather))
    res.sort(key=itemgetter(1), reverse=True)
    res = int("".join([str(t[0] + 1) for t in res]))
    ans += res

print(ans)
