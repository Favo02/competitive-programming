cases = int(input())

X = 0
Y = 1

def toLinear(p, f):
  if p[Y] == 0: return p[X]
  if p[X] == f[X]-1: return f[X]-1 + p[Y]
  if p[Y] == f[Y]-1: return f[X]-1 + f[Y]-1 + (f[X]-1-p[X])
  if p[X] == 0: return f[X]*2-2 + f[Y]-1 + (f[Y]-1-p[Y])

for _ in range(cases):
  tokens = input().split(" ")
  field = int(tokens[0])+1, int(tokens[1])+1
  train = int(tokens[2]), int(tokens[3])
  filippo = int(tokens[4]), int(tokens[5])

  # print(field, train, filippo)

  dists = {
    (filippo[X],field[Y]-1): field[Y]-1 - filippo[Y],
    (filippo[X],0): filippo[Y],
    (0, filippo[Y]): filippo[X],
    (field[X]-1, filippo[Y]): field[X]-1 - filippo[X],
  }

  traLin = toLinear(train, field)

  Min = 10**9
  for pos, dist in dists.items():
    res = 0
    filLin = toLinear(pos, field)
    timeToReach = traLin - filLin

    # print(pos, filLin, traLin, timeToReach)

    if timeToReach < dist:
      res = timeToReach + (field[X]*2-2 + field[Y]*2-2)
    else:
      res = timeToReach

    Min = min(Min, res)

  print(Min)
