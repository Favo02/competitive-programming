import sys

lines = sys.stdin.read().strip().splitlines()
items = []

for item in lines:
  tokens = item.replace(",", "").split()
  assert len(tokens) == 13
  code, qlty, cost, mat = tokens[1], int(tokens[5]), int(tokens[8]), int(tokens[12])
  items.append((qlty, cost, mat, code))

items.sort(reverse=True)
print(sum(i[2] for i in items[:5]))
