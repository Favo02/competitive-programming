
paths = int(input())
dir = {"W":(0, -1), "S":(0, 1), "D":(1,0), "A":(-1, 0)}

for _ in range(paths):
  x, y = 0, 0
  path = input()

  maxx, minx = 0, 0
  maxy, miny = 0, 0

  for s in path:
    if s not in dir: continue
    dx, dy = dir[s]
    x, y = x+dx, y+dy

    maxx = max(maxx, x)
    minx = min(minx, x)

    maxy = max(maxy, y)
    miny = min(miny, y)

  print(maxx-minx +1 , maxy - miny +1)


