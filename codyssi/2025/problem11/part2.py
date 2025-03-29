import sys
import string

lines = sys.stdin.read().strip().splitlines()
summ = 0

bases = "0123456789" + string.ascii_uppercase + string.ascii_lowercase + "!@#$%^"

for line in lines:
  num, base = line.split()
  base = int(base)
  num10 = 0

  for i, n in enumerate(reversed(num)):
    num10 += bases.index(n)*(base**i)

  summ += num10

res = []
while summ >= 68:
  res.append(bases[summ % 68])
  summ //= 68
res.append(bases[summ % 68])

print("".join(reversed(res)))
