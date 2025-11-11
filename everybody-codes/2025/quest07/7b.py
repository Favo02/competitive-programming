import sys

names, rules = sys.stdin.read().strip().split("\n\n")
names = names.split(",")
rules = [r.split(" > ") for r in rules.split("\n")]
rules = {a: b.split(",") for a, b in rules}

def check(name):
    for i, c in enumerate(name[:-1]):
        if name[i+1] not in rules[c]:
            return False
    return True

print(sum(i+1 for i, n in enumerate(names) if check(n)))
