from collections import defaultdict
from itertools import combinations_with_replacement
import sys

numbers, rawcards = sys.stdin.read().split("\n\n")
numbers = list(map(int, (" ".join(map(str.strip, numbers.splitlines()))).split()))
time = {n: i for i, n in enumerate(numbers)}
index = defaultdict(list)
cubes = []

for card in rawcards.splitlines():
    face = list(map(int, card.split()))
    if cubes and len(cubes[-1]) < 5:
        cubes[-1].append([face[i * 5 : (i + 1) * 5] for i in range(5)])
    else:
        cubes.append([[face[i * 5 : (i + 1) * 5] for i in range(5)]])

for x in range(5):
    for y in range(5):
        for z in range(5):
            for k in range(5):
                index[cubes[x][y][z][k]].append((x, y, z, k))


def isbingo(cube, x, y, z, k, seen):
    dirs = combinations_with_replacement((0, +1, -1), 4)
    bingo = 0
    for dx, dy, dz, dk in dirs:
        if dx == dz == dy == dk == 0:
            continue
        els = []
        for m in range(-4, 5):
            if not (0 <= (x + dx * m) < 5):
                continue
            if not (0 <= (y + dy * m) < 5):
                continue
            if not (0 <= (z + dz * m) < 5):
                continue
            if not (0 <= (k + dk * m) < 5):
                continue
            els.append(cube[x + dx * m][y + dy * m][z + dz * m][k + dk * m])
        assert len(els) <= 5
        if len(els) == 5 and all(s in seen for s in els):
            bingo += 1
    return bingo


bingos = 0
for i, n in enumerate(numbers):
    for x, y, z, k in index[n]:
        bingos += isbingo(cubes, x, y, z, k, set(numbers[: i + 1]))
    if bingos >= 5:
        print(n)
        break
