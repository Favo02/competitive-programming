import sys

def fam(P1, P2, C):
    if any(c not in [p1, p2] for p1, p2, c in zip(P1, P2, C)):
        return 0
    return sum(1 for a, b in zip(P1, C) if a == b) * sum(1 for a, b in zip(P2, C) if a == b)

dnas = list(map(lambda l: l.strip().split(":")[1], sys.stdin.readlines()))

res = 0
for i, p1 in enumerate(dnas):
    for ii, p2 in enumerate(dnas):
        if i <= ii: continue
        for iii, c in enumerate(dnas):
            if i == iii: continue
            if ii == iii: continue
            res += fam(p1, p2, c)
print(res)
