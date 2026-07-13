import sys

rules = list(map(lambda l: l.strip().split(), sys.stdin.readlines()))
rules = {frozenset({r[0], r[1]}): r[2:] for r in rules}

stoats = ["A", "B"]

for i in range(7):
    newstoats = [stoats[0]]
    for a, b in zip(stoats, stoats[1:]):
        if frozenset({a, b}) in rules:
            newstoats += rules[frozenset({a, b})]
        newstoats.append(b)
    stoats = newstoats

print(len(stoats))
