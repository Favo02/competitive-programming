import sys
import re
from collections import defaultdict, deque

P, T = sys.stdin.read().split("\n\n\n")
plants = P.split("\n\n")
tests = [list(map(int, t.split())) for t in T.splitlines()]

thickness = {}
revgraph = defaultdict(list)
energies = defaultdict(int)

for id, pl in enumerate(plants):
    plant, *branches = pl.split("\n")
    thickness[id+1] = int(re.search(r'thickness (-?\d+)', plant).group(1))

    for branch in branches:
        if not branch: continue
        if "free" in branch:
            to = -1
        else:
            to = int(re.search(r'Plant (-?\d+)', branch).group(1))
        thick = int(re.search(r'thickness (-?\d+)', branch).group(1))

        revgraph[id+1].append((to, thick))

def backbfs():
    q = deque()
    q.append((len(plants), 1))
    energies = defaultdict(int)
    energies[len(plants)] = 1
    while q:
        cur, en = q.popleft()

        for to, thick in revgraph[cur]:
            if to == -1:
                continue
            energies[to] += en * thick
            q.append((to, en*thick))
    return energies

def simulate(test):
    energies = defaultdict(int)

    for id in thickness.keys():
        if id <= len(test):
            energies[id] = test[id-1]
            continue

        energy = 0
        for to, thick in revgraph[id]:
            if to == -1:
                continue
            energy += energies[to] * thick

        energies[id] = energy if energy >= thickness[id] else 0

    return energies

backtrack = backbfs()
besttest = [1 if backtrack[i] >= 0 else 0 for i in range(1, len(tests[0])+1)]
bestval = simulate(besttest)[len(plants)]

res = 0
for t in tests:
    val = simulate(t)[len(plants)]
    assert val <= bestval
    if val == 0: continue
    res += bestval - val
print(res)
