from collections import deque, defaultdict
from operator import itemgetter
import sys

rawtrees = sys.stdin.read().split("\n\n")


def pprint(tree, stems):
    minx = min(map(itemgetter(0), tree.keys()))
    maxx = max(map(itemgetter(0), tree.keys()))
    miny = min(map(itemgetter(1), tree.keys()))
    maxy = max(map(itemgetter(1), tree.keys()))
    for y in range(maxy, miny - 1, -1):
        print(f"{y + 1:02d}:", end="")
        for x in range(minx - 1, maxx + 2):
            if (x, y) in tree:
                if (x, y) in stems:
                    print("@", end="")
                else:
                    print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def energy(tree, stems, t):
    pieces = list(tree.keys())
    pieces.sort(key=lambda p: (-p[1], p[0]))
    above = defaultdict(int)
    energy = 0
    for x, y in pieces:
        if (x, y) in tree and (x, y) not in stems:
            if tree[(x, y)][1] == t:
                energy += min(y + 1, 10) * max(3 - above[x], 0)
            above[x] += 1
    return energy


def place(x, y, what, day, t):
    if what == "XX":
        return
    if (x, y) in tree:
        val, tt = tree[(x, y)]
        if tt == t and val < what:
            tree[(x, y)] = what, t
    else:
        tree[(x, y)] = (what, t)
        queue.append((x, y, day + 1, t))
        stems.add((x, y))


tree = {}
queue = deque()
stems = set()
dnas = {}

res = 0
for j, tr in enumerate(rawtrees):
    top, main = tr.strip().split("\n")
    top = list(filter(lambda e: e, top.split(" ")))
    main = list(filter(lambda e: e, main.split(" ")))
    for i, t in enumerate(top):
        dnas[(main[3 * i + 1], j)] = (main[3 * i], t, main[3 * i + 2])
    tree[(j * 10, 0)] = ("00", j)
    queue.append((j * 10, 0, 1, j))
    stems.add((j * 10, 0))

lastd = 0
stopped = set()
while queue:
    x, y, d, t = queue.popleft()
    if t in stopped:
        continue
    if lastd != d:
        lastd = d
        # print("day", d)
        # pprint(tree, stems)
        for et in range(len(rawtrees)):
            req = len(list((filter(lambda v: v[1] == et, tree.values())))) * 3
            en = energy(tree, stems, et)
            if d > 5 and req > en:
                stopped.add(et)
    if t in stopped:
        continue

    if d > 100:
        break
    stems.discard((x, y))
    what, tt = tree[(x, y)]
    assert tt == t
    (left, top, right) = dnas[(what, t)]
    place(x - 1, y, left, d, t)
    place(x, y + 1, top, d, t)
    place(x + 1, y, right, d, t)

# pprint(tree, stems)

print(len(tree))
