import sys

def manDist(a, b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(1, len(lines), 2):
  # print()
  points = lines[i+1].split(" ")
  points = [int(p) for p in points]
  points.sort()
  print(points)

  reserve = None
  if len(points) // 2 % 2 != 0:
    reserve = (points[len(points)//2-1], points[len(points)//2])
    points = points[:len(points)//2-1] + points[len(points)//2+1:]

  # print(points, reserve)

  even = [a for k,a in enumerate(points) if k % 2 == 0]
  odd = [a for k,a in enumerate(points) if k % 2 == 1]
  # print(even, odd)

  couples = []
  for j in range(0, len(even), 2):
    couples.append((even[j], even[j+1]))
    couples.append((odd[j], odd[j+1]))

  if reserve is not None:
    couples.append(reserve)

  # print(couples)

  dist = 0
  for c in range(len(couples)-1):
    dist += manDist(couples[c], couples[c+1])

  print(dist)
  for c in couples:
    print(c[0], c[1])
