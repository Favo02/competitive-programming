import sys

rows = [[] for _ in range(4)]
cols = [[] for _ in range(4)]

for row, line in enumerate(sys.stdin):
  for col, char in enumerate(line.strip()):
    if char != "*" and char != ".":
      if 2 <= col < 6:
        cols[col-2].append(char)
      else:
        rows[row-2].append(char)

res = []

for r in range(4):
  for c in range(4):
    available = rows[r] + cols[c]

    for i, char in enumerate(available):
      if char in available[i+1:]:
        res.append(char)
        break

print("".join(res))
