import sys
from collections import defaultdict, deque

PORT, tp = sys.stdin.read().strip().split("\n\n")

PORT = int(PORT.split(": ")[1])
tp = [tuple(map(int, a.strip().split())) for a in tp.splitlines()]
TP = defaultdict(set)
for a, b in tp:
    TP[a - 1].add(b - 1)
    TP[b - 1].add(a - 1)


def bfs(st, tp):
    queue = deque()
    queue.append((st, 0))
    seen = set()
    tot = 0
    while queue:
        cur, d = queue.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        tot += d
        jumps = {(cur + i) % PORT for i in range(1, 4)} | {
            (cur - i) % PORT for i in range(1, 4)
        }
        if tp:
            jumps |= TP[cur]
        for adj in jumps:
            if adj in seen:
                continue
            queue.append((adj, d + 1))
    return tot


def pairs(rem):
    if not rem:
        return {frozenset()}

    a = next(iter(rem))
    res = set()
    for b in rem - {a}:
        for rest in pairs(rem - {a, b}):
            res.add(rest | frozenset({(a, b)}))
    return res


notp = bfs(0, False) * PORT

OLDTP = defaultdict(set, {k: v.copy() for k, v in TP.items()})
# print(OLDTP)
bestsitp = float("inf")
distp = PORT // 8
for pos in range(PORT // 8):
    poss = [pos + distp * i for i in range(8)]
    # print(poss)

    for pa in pairs(set(poss)):
        valid = True
        # print("-----------", pa)
        # print(TP)
        for a, b in pa:
            # print(a, b)
            if a in TP[b]:
                valid = False
                assert b in TP[a]
                break
            assert a not in TP[b]
            assert b not in TP[a]
            TP[a].add(b)
            TP[b].add(a)
            # print(TP)

        if valid:
            sitp = 0
            for start in range(PORT):
                sitp += bfs(start, True)
            bestsitp = min(bestsitp, sitp)

        TP = defaultdict(set, {k: v.copy() for k, v in OLDTP.items()})

# print(bestsitp)
print(notp - bestsitp)
