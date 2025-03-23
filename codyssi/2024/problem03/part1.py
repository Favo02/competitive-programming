import sys

res = 0
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  a, base = l.split()
  res += int(base)

print(res)
