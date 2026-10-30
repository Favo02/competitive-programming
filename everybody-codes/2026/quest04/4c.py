import sys
from collections import defaultdict

lines = sys.stdin.readlines()

times = []
quests = set()
players = set()

for line in lines:
    tokens = line.strip().split()
    idd, quest, part, time = (int(x.split("=")[1]) for x in tokens)
    times.append((idd, quest, part, time))
    quests.add(quest)
    players.add(idd)

res = defaultdict(int)

for quest in sorted(quests):
    time = defaultdict(int)
    for part in range(1, 4):
        # print(quest, part)
        valid = set()
        for i, q, p, t in times:
            if q == quest and p == part:
                time[i] += t
                valid.add(i)

        score = sorted((time[p], p) for p in valid)

        points = {1: 51, 2: 101, 3: 151}[part]
        last = None
        skip = 1
        for s, p in score:
            if last != s:
                points -= skip
                skip = 1
            else:
                skip += 1
            if points <= 0:
                break
            res[p] += points
            last = s
        # print(list(res.items()))

# print(sorted(res.values(), reverse=True))

ans = 0
pos = 0
last = 0
skip = 1
for t in sorted(res.values(), reverse=True):
    if t != last:
        pos += skip
        skip = 1
    else:
        skip += 1
    ans += pos * t
    last = t
print(ans)
