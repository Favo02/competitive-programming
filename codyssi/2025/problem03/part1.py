import sys

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for line in lines:
  (a, b), (c, d) = map(lambda l: map(int, l.split("-")), line.split())

  res += b-a+1 + d-c+1

print(res)
