import sys
import string
import math

def encode(base, summ):
  reslen = 1
  while summ >= base:
    reslen += 1
    summ //= base
  return reslen

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

base = 2
while encode(base, summ) > 4:
  base += 1
print(base)
