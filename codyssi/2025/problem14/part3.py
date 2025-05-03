import sys
from functools import reduce

lines = sys.stdin.read().strip().splitlines()
items = []

for item in lines:
  tokens = item.replace(",", "").split()
  assert len(tokens) == 13
  code, qlty, cost, mat = tokens[1], int(tokens[5]), int(tokens[8]), int(tokens[12])
  if cost > 30:
    continue
  items.append((code, qlty, cost, mat))

items.sort(key=lambda i: (i[3], i[2]))

# BUDGET = 150 # example
BUDGET = 300

dp = [(0, 0)] * (BUDGET+1)
for code, qlty, cost, mat in items:
  newdp = dp.copy()
  for i, (q, m) in enumerate(dp):
    if i > 0 and (q, m) == (0, 0):
      continue
    if i + cost > BUDGET:
      continue
    new = (q + qlty, (m - mat))
    if new > newdp[i+cost]:
      newdp[i+cost] = new

  dp = newdp

q, m = max(dp)
print(q * -m)
