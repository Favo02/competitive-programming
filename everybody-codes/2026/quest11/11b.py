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


notp = bfs(0, False) * PORT

bestsitp = float("inf")
for an in range(PORT):
    for bn in range(an + 1, PORT):
        if an in TP[bn]:
            assert bn in TP[an]
            continue
        assert an not in TP[bn]
        assert bn not in TP[an]
        TP[an].add(bn)
        TP[bn].add(an)

        sitp = 0
        for start in range(PORT):
            sitp += bfs(start, True)

        TP[an].discard(bn)
        TP[bn].discard(an)

        bestsitp = min(bestsitp, sitp)

print(notp - bestsitp)
