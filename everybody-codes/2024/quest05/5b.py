import sys
from collections import defaultdict

def round(turn):
  clapper = field[turn].pop(0)
  toinsert = clapper

  targetcol = (turn + 1) % 4
  SIZE = len(field[targetcol])

  clapper -= 1
  clapper %= (SIZE*2)

  if clapper < SIZE:
    field[targetcol].insert(clapper, toinsert)
  else:
    field[targetcol].insert(SIZE - (clapper - SIZE), toinsert)

  return int(str(field[0][0]) + str(field[1][0]) + str(field[2][0]) + str(field[3][0]))


field = [[] for _ in range(4)]

for line in sys.stdin:
  line = map(int, line.strip().split())
  for i, l in enumerate(line):
    field[i].append(l)

seen = defaultdict(int)

turn = 0
while True:
  top = round(turn % 4)
  seen[top] += 1
  # print(top)

  if seen[top] == 2024:
    print(top * (turn+1))
    break

  turn += 1
