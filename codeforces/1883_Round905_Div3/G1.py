import sys

lines = []
for l in sys.stdin:
  lines.append(l[:-1])
lines = lines[1:]

for i in range(0, len(lines), 3):
  a = lines[i+1].split(" ")
  a = [int(aa) for aa in a]
  a.insert(0, 1)
  b = lines[i+2].split(" ")
  b = [int(bb) for bb in b]

  a.sort()
  b.sort()

  print(a)
  print(b)
  res = 0
  while True:
    for aa, bb in zip(a,b):
      if bb-aa <= 0:
        res += 1
        b = b[1:]
        a = a[:-1]
        break
    else:
      break
  print(res)
