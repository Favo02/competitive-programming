import sys
import re
from collections import defaultdict

P, T = sys.stdin.read().split("\n\n\n")
plants = P.split("\n\n")
tests = T.splitlines()
energies = defaultdict(int)

def simulate(test):
    for id, pl in enumerate(plants):
        if id < len(test):
            energies[id+1] = int(test[id])
            continue

        plant, *branches = pl.split("\n")
        thickness = int(re.search(r'thickness (-?\d+)', plant).group(1))

        energy = 0

        for branch in branches:
            if not branch: continue
            if "free" in branch:
                to = -1
                energy += 1
            else:
                to = int(re.search(r'Plant (-?\d+)', branch).group(1))
                thick = int(re.search(r'thickness (-?\d+)', branch).group(1))
                energy += energies[to] * thick

        energies[id+1] = energy if energy >= thickness else 0
    return energies[len(plants)]

print(sum(simulate(list(map(int, t.split()))) for t in tests))
