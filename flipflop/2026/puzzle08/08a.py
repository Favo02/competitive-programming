import sys
from collections import defaultdict

rawrules = list(map(lambda l: l.strip().split(), sys.stdin.readlines()))
rules = {}
for r in rawrules:
    if r[0] in rules: continue
    rules[r[0]] = r[1:]

stoats = {"A":1, "B":1}

for i in range(7):
    newstoats = defaultdict(int)
    for k, v in stoats.items():
        for ev in rules[k]:
            newstoats[ev] += v
    stoats = newstoats

print(sum(stoats.values()))
