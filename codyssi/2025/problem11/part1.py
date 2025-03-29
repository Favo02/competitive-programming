import sys
import string

lines = sys.stdin.read().strip().splitlines()
res = 0

bases = "0123456789" + string.ascii_uppercase + string.ascii_lowercase

for line in lines:
  num, base = line.split()
  base = int(base)
  num10 = 0

  for i, n in enumerate(reversed(num)):
    num10 += bases.index(n)*(base**i)

  res = max(res, num10)

print(res)
