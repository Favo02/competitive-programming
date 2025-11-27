import sys
from math import sqrt, ceil
from collections import defaultdict

lines = list(map(str.strip, sys.stdin.readlines()))

Xv = Yv = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == "@":
            Xv, Yv = x, y

R = 10
res = 0

destr = defaultdict(lambda: 0)

for Yc, line in enumerate(lines):
    for Xc, cell in enumerate(line):
        if cell == "@": continue
        dist = ceil(sqrt((Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc)))
        destr[dist] += int(cell)

k, v = max((v, k) for k, v in destr.items())
print(k * v)
