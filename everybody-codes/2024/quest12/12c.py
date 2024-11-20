import sys

def save(x, y, val, time):
  if (x, y) in precalc:
    if precalc[(x,y)][1] > val:
      precalc[(x,y)] = (time, val)
  else:
    precalc[(x,y)] = (time, val)

def simulate(sx, sy, speed):
  time = 0

  save(sx, sy, speed, time)
  save(sx, sy+1, speed*2, time)
  save(sx, sy+2, speed*3, time)

  for _ in range(speed):
    sx += 1
    sy += 1
    time += 1
    save(sx, sy, speed, time)
    save(sx, sy+1, speed*2, time)
    save(sx, sy+2, speed*3, time)

  for _ in range(speed):
    sx += 1
    time += 1
    save(sx, sy, speed, time)
    save(sx, sy+1, speed*2, time)
    save(sx, sy+2, speed*3, time)

  while sy >= 0:
    sx += 1
    sy -= 1
    time += 1
    save(sx, sy, speed, time)
    save(sx, sy+1, speed*2, time)
    save(sx, sy+2, speed*3, time)

cannons = [(0,0), (0,1), (0,2)]
targets = []

max_x = 0

for line in sys.stdin:
  x, y = map(int, line.strip().split())
  targets.append((x,y))
  max_x = max(max_x, x)

precalc = {}

for speed in range(1, max_x // 2 + 10):
  simulate(0, 0, speed)

res = 0
for x, y in targets:

  curres = float("inf")
  time = 0

  while y >= 0 and x >= 0:

    if (x, y) in precalc:
      t, val = precalc[(x, y)]
      if t <= time:
        curres = min(curres, val)
        break

    time += 1
    x -= 1
    y -= 1

  assert curres != float("inf")
  res += curres

print(res)
