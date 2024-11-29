import sys

def left(r, c):
  temp = field[r-1][c-1]
  field[r-1][c-1] = field[r-1][c]
  field[r-1][c] = field[r-1][c+1]
  field[r-1][c+1] = field[r][c+1]
  field[r][c+1] = field[r+1][c+1]
  field[r+1][c+1] = field[r+1][c]
  field[r+1][c] = field[r+1][c-1]
  field[r+1][c-1] = field[r][c-1]
  field[r][c-1] = temp

def right(r, c):
  temp = field[r-1][c-1]
  field[r-1][c-1] = field[r][c-1]
  field[r][c-1] = field[r+1][c-1]
  field[r+1][c-1] = field[r+1][c]
  field[r+1][c] = field[r+1][c+1]
  field[r+1][c+1] = field[r][c+1]
  field[r][c+1] = field[r-1][c+1]
  field[r-1][c+1] = field[r-1][c]
  field[r-1][c] = temp

key = input()
input()

field = []
for line in sys.stdin:
  line = line.strip()
  field.append(list(line))

op = {"L": left, "R": right}

k = 0

for r, row in enumerate(field):
  for c, cell in enumerate(row):
    if r == 0 or r == len(field)-1: continue
    if c == 0 or c == len(field[0])-1: continue

    op[key[k % len(key)]](r, c)
    k += 1

for f in field:
  if ">" in f:
    print("".join(f[f.index(">")+1 : f.index("<")]))
