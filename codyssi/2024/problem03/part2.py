import sys

res = 0
lines = sys.stdin.read().strip().splitlines()

for l in lines:
  num, base = l.split()
  res += int(num, int(base))

print(res)
