import sys

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

res = 0
seen = set()

turn = 0
while True:
  top = round(turn % 4)
  res = max(res, top)

  t = (tuple(field[0]), tuple(field[1]), tuple(field[2]), tuple(field[3]))
  if t in seen: break
  seen.add(t)

  turn += 1

print(res)
