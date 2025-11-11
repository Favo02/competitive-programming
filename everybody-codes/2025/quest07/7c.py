import sys
from collections import deque

prefixes, rules = sys.stdin.read().strip().split("\n\n")
prefixes = prefixes.split(",")
rules = [r.split(" > ") for r in rules.split("\n")]
rules = {a: b.split(",") for a, b in rules}

def check(name):
    for i, c in enumerate(name[:-1]):
        if name[i+1] not in rules[c]:
            return False
    return True

def walk(prefix):
    queue = deque()
    queue.append(prefix)
    while queue:
        name = queue.popleft()
        if len(name) >= 7:
            names.add(name)
        if len(name) == 11:
            continue
        for nnext in rules.get(name[-1], []):
            queue.append(name + nnext)

names = set()
for prefix in prefixes:
    if not check(prefix):
        continue
    walk(prefix)
print(len(names))
