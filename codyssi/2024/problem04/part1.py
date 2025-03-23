import sys

locations = set()
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  a, b = l.split(" <-> ")
  locations.add(a)
  locations.add(b)

print(len(locations))
