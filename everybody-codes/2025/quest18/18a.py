import sys
import re
from collections import defaultdict

plants = sys.stdin.read().split("\n\n")
energies = defaultdict(int)

for id, pl in enumerate(plants):
    plant, *branches = pl.split("\n")
    thickness = int(re.search(r'thickness (\d+)', plant).group(1))

    energy = 0

    for branch in branches:
        if not branch: continue
        if "free" in branch:
            to = -1
            energy += 1
        else:
            to = int(re.search(r'Plant (\d+)', branch).group(1))
            thick = int(re.search(r'thickness (\d+)', branch).group(1))
            energy += energies[to] * thick

    energies[id+1] = energy if energy >= thickness else 0

print(energies[len(plants)])
