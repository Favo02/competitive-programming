import sys

seen = set()

for line in sys.stdin:
  steps = line.strip().split(",")

  x = y = z = 0
  for s in steps:
    dir, qty = s[0], int(s[1:])

    dx = dy = dz = 0
    if dir == "U": dy = 1
    if dir == "D": dy = -1
    if dir == "R": dx = 1
    if dir == "L": dx = -1
    if dir == "F": dz = 1
    if dir == "B": dz = -1

    for _ in range(qty):
      x += dx
      y += dy
      z += dz
      seen.add((x,y,z))

print(len(seen))
