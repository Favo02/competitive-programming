import sys

lines = list(map(str.strip, sys.stdin.readlines()))

minn = float("inf")
maxx = 0

for line in lines:
  a, b = line.split(", ")
  a = int(a[1:])
  b = int(b[:-1])
  dist = abs(a) + abs(b)
  minn = min(minn, dist)
  maxx = max(maxx, dist)

print(maxx - minn)
