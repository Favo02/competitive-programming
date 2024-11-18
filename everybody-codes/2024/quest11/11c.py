import sys
from collections import defaultdict

ev = {}

for line in sys.stdin:
  fromm, to = line.strip().split(":")
  ev[fromm] = to.split(",")

def calc(start, day):
  therm = {start: 1}

  for _ in range(day):
    newtherm = defaultdict(int)
    for t, qty in therm.items():
      for tt in ev[t]:
        newtherm[tt] += qty
    therm = newtherm

  return sum(therm.values())

minn = float("inf")
maxx = 0

for s in ev.keys():
  c = calc(s, 20)
  maxx = max(maxx, c)
  minn = min(minn, c)

print(maxx - minn)
