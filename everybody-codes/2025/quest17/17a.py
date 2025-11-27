import sys

lines = list(map(str.strip, sys.stdin.readlines()))

Xv = Yv = None
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == "@":
            Xv, Yv = x, y

R = 10
res = 0

for Yc, line in enumerate(lines):
    for Xc, cell in enumerate(line):
        if cell == "@": continue
        if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R:
            res += int(cell)

print(res)
