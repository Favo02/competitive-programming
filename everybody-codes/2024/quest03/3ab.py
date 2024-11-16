import sys

res = 0

field = []
for line in sys.stdin:
  field.append(list(map(lambda x: 1 if x == "#" else 0, list(line.strip()))))
  res += field[-1].count(1)

DIRS = [(0,-1),(0,+1),(-1,0),(+1,0)]
ROWS = len(field)
COLS = len(field[0])

edit = True
while edit:
  edit = False

  for r, row in enumerate(field):
    for c, col in enumerate(row):
      if col == 0: continue


      for dr, dc in DIRS:
        if not (0 <= r+dr < ROWS): continue
        if not (0 <= c+dc < COLS): continue

        if abs(field[r+dr][c+dc] - (col+1)) > 1:
          break
      else:
        edit = True
        field[r][c] += 1
        res += 1

print(res)
