import sys
from collections import defaultdict
from operator import itemgetter

lines = sys.stdin.readlines()

players = defaultdict(int)

for line in lines:
    tokens = line.strip().split()
    idd, quest, part, time = (int(x.split("=")[1]) for x in tokens)
    players[idd] += time

standings = sorted(players.items(), key=itemgetter(1))
res = sum(((i + 1) * t for i, (p, t) in enumerate(standings)))

print(res)
