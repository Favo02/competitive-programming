import sys
from collections import defaultdict

lines = sys.stdin.readlines()

timee = defaultdict(int)
parts = defaultdict(int)

for line in lines:
    tokens = line.strip().split()
    idd, quest, part, time = (int(x.split("=")[1]) for x in tokens)
    timee[idd] += time
    parts[idd] += 1


total = sorted([(parts[p], t) for p, t in timee.items()], key=lambda x: (-x[0], x[1]))
res = sum(((i + 1) * t for i, (p, t) in enumerate(total)))

print(res)
