import sys

inst, sushi = sys.stdin.read().split("\n\n")
inst = inst.strip()

sushi = list(map(lambda s: (int(s.strip().split(",")[0]), int(s.strip().split(",")[1])), sushi.split()))

DIRS = {">": (1, 0), "v": (0, -1), "<": (-1, 0), "^": (0, 1)}

i = 0
x = y = 0
for d in inst[:2500]:
    dx, dy = DIRS[d]
    x += dx
    y += dy
    if sushi[i] == (x, y):
        i += 1
print(i)

