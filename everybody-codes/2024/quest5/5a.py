import sys

def round(turn):
  clapper = field[turn].pop(0)

  targetcol = (turn + 1) % 4
  if clapper <= len(field[targetcol]):
    field[targetcol].insert(clapper-1, clapper)
  else:
    field[targetcol].insert(clapper, clapper)


field = [[] for _ in range(4)]

for line in sys.stdin:
  line = map(int, line.strip().split())
  for i, l in enumerate(line):
    field[i].append(l)

for turn in range(10):
  round(turn % 4)

print(field[0][0], field[1][0], field[2][0], field[3][0], sep="")
