import sys

def solve(field):
  rows = [[] for _ in range(4)]
  cols = [[] for _ in range(4)]

  for row, line in enumerate(field):
    for col, char in enumerate(line):
      if char != "*" and char != ".":
        if 2 <= col < 6:
          cols[col-2].append(char)
        else:
          rows[row-2].append(char)

  res = 0

  for r in range(4):
    for c in range(4):
      available = rows[r] + cols[c]

      for i, char in enumerate(available):
        if char in available[i+1:]:
          res += (ord(char) - ord("A") + 1) * (r*4 + (c+1))
          break

  return res

res = 0

fields = [[] for _ in range(15)]

for line in sys.stdin:
  if line == "\n":
    for f in fields:
      res += solve(f)
    fields = [[] for _ in range(15)]
    continue

  tokens = line.strip().split()
  for i, t in enumerate(tokens):
    fields[i].append(t)

for f in fields:
  res += solve(f)

print(res)
