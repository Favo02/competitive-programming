import sys

def hit(x, y, speed, cannon):
  res = 0
  if (x, y) in targets:
    res = (speed * cannon) * targets[(x, y)]
    del targets[(x, y)]
  return res

def simulate(x, y, speed, cannon):
  res = 0

  for _ in range(speed):
    x += 1
    y += 1
    res += hit(x, y, speed, cannon)

  for _ in range(speed):
    x += 1
    res += hit(x, y, speed, cannon)

  while y >= 0:
    x += 1
    y -= 1
    res += hit(x, y, speed, cannon)

  return res

field = []
for y, line in enumerate(sys.stdin):
  line = line.strip()
  if all(l == "=" for l in line):
    ground = y
    break
  field.append(line)

cannons = []
targets = {}

for y, line in enumerate(field):
  for x, cell in enumerate(line):
    if cell == "T":
      targets[(x, ground-1-y)] = 1
    if cell == "H":
      targets[(x, ground-1-y)] = 2
    if cell in ["A", "B", "C"]:
      cannons.append((x, ground-1-y))

cannons.sort()

res = 0

for seg, c in enumerate(cannons):
  for speed in range(1, 100):
    res += simulate(*c, speed, seg+1)

assert len(targets) == 0

print(res)
