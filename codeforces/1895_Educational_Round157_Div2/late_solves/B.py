import sys

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(1, len(lines), 2):
  points = lines[i+1].split(" ")
  points = [int(p) for p in points]
  points.sort()

  x = points[:len(points)//2]
  y = points[len(points)//2:]

  print((x[-1]-x[0]) + (y[-1]-y[0]))
  couples = []
  for xx,yy in zip(x,y):
    print(xx, yy)
