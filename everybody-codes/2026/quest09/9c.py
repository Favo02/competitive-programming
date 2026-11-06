import sys
from heapq import heappop, heappush

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for ii, line in enumerate(lines):
    idd, growth, limit = line.split(", ")
    idd = idd.split("=")[1]
    growth = int(growth.split("=")[1])
    limit = int(limit.split("=")[1])

    if limit == 1:
        res += 1
        continue

    branches = []
    heappush(branches, (growth, 1))
    elements = 1
    last = -1
    stop = False
    while True:
        ttime, qty = heappop(branches)
        elements += qty
        if stop and ttime != last:
            # print(ii, ttime, elements)
            res += last
            break

        heappush(branches, (ttime + growth - 1, qty))
        heappush(branches, (ttime + (growth - (growth // 2)), qty * 2))

        if elements >= limit:
            stop = True
        last = ttime

print(res)
