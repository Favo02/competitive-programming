import sys

lines = list(map(str.strip, sys.stdin.readlines()))

boxes = []

res = 0
for line in lines:
  (a, b), (c, d) = map(lambda l: map(int, l.split("-")), line.split())
  ranges = set()
  for e in range(a, b+1):
    ranges.add(e)
  for e in range(c, d+1):
    ranges.add(e)
  boxes.append(ranges)

for a, b in zip(boxes, boxes[1:]):
  res = max(res, len(a | b))

print(res)
