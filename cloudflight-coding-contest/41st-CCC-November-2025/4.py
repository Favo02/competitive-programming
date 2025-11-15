from collections import deque
from math import ceil

def pace(station):
    res = []
    cur = 5
    for _ in range(ceil(abs(station) / 2)+1):
        res.append(paces[cur])
        nextcur = (cur + 1) if station > 0 else (cur - 1)
        cur = max(0, min(len(paces)-1, nextcur))

    if station % 2 == 1:
        res += (res[:-1])[::-1]
    else:
        res += res[::-1]

    return " ".join(map(str, res))


n = int(input())

paces = [-1, -2, -3, -4, -5, 0, 5, 4, 3, 2, 1]
for _ in range(n):
    station, timelimit = input().split()
    sx, sy = map(int, station.split(","))

    X = pace(sx)
    Y = pace(sy)

    print(X)
    print(Y)
    print()

