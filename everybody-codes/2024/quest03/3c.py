import sys

res = 0

field = []
for line in sys.stdin:
  field.append(list(map(lambda x: 1 if x == "#" else 0, list(line.strip()))))
  field[-1].insert(0, 0)
  field[-1].append(0)
  res += field[-1].count(1)

COLS = len(field[0])

field.insert(0, [0] * COLS)
field.append([0] * COLS)

DIRS = [(0,-1),(0,+1),(-1,0),(+1,0),(+1,+1),(-1,-1),(-1,+1),(+1,-1)]

edit = True
while edit:
  edit = False

  for r, row in enumerate(field):
    for c, col in enumerate(row):
      if col == 0: continue

      for dr, dc in DIRS:
        if abs(field[r+dr][c+dc] - (col+1)) > 1:
          break
      else:
        edit = True
        field[r][c] += 1
        res += 1

print(res)
