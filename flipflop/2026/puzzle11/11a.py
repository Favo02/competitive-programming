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
        print(y + 1, end=" ")
        for x in range(minx, maxx + 1):
            if (x, y) in tree:
                if (x, y) in stems:
                    print("@", end="")
                else:
                    print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


def energy(tree, stems):
    pieces = list(tree.keys())
    pieces.sort(key=lambda p: (-p[1], p[0]))
    above = defaultdict(int)
    energy = 0
    for x, y in pieces:
        if (x, y) in tree and (x, y) not in stems:
            energy += min(y + 1, 10) * max(3 - above[x], 0)
            above[x] += 1
    return energy


def solve(dnas):
    def place(x, y, what, day):
        if what == "XX":
            return
        if (x, y) in tree:
            tree[(x, y)] = max(tree[(x, y)], what)
        else:
            tree[(x, y)] = what
            queue.append((x, y, day + 1))
            stems.add((x, y))

    tree = {}
    tree[(0, 0)] = "00"
    queue = deque()
    queue.append((0, 0, 1))
    stems = set()
    lastd = 0
    while queue:
        x, y, d = queue.popleft()
        if lastd != d:
            lastd = d
            # print("day", d)
            # pprint(tree, stems)
            req = len(tree) * 3
            en = energy(tree, stems)
            if d > 5 and req > en:
                break

        if d > 100:
            break
        stems.discard((x, y))
        what = tree[(x, y)]
        (left, top, right) = dnas[what]
        place(x - 1, y, left, d)
        place(x, y + 1, top, d)
        place(x + 1, y, right, d)
    return len(tree)


res = 0
for tree in rawtrees:
    top, main = tree.strip().split("\n")
    top = list(filter(lambda e: e, top.split(" ")))
    main = list(filter(lambda e: e, main.split(" ")))
    dnas = {}
    for i, t in enumerate(top):
        dnas[main[3 * i + 1]] = (main[3 * i], t, main[3 * i + 2])
    res += solve(dnas)
print(res)
