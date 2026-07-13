import sys
from collections import defaultdict

rawrules = list(map(lambda l: l.strip().split(), sys.stdin.readlines()))
rules = {(r[0], r[1]): r[2:] for r in rawrules}
rules |= {(r[1], r[0]): r[2:] for r in rawrules}

stoats = {("A", "B"): 1}

for i in range(21):
    newstoats = defaultdict(int)

    for (a, b), qty in stoats.items():
        neww = rules[(a, b)]
        newstoats[(a, neww[0])] += qty
        for c, d in zip(neww, neww[1:]):
            newstoats[(c, d)] += qty
        newstoats[(neww[-1], b)] += qty
    stoats = newstoats

print(sum(stoats.values()) + 1)
