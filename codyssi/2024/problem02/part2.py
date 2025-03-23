import sys

res = 0
lines = [l == "TRUE" for l in sys.stdin.read().strip().splitlines()]

for i, (a, b) in enumerate(zip(lines[::2], lines[1::2])):
  if ((i % 2 == 0) and (a and b)) or ((i % 2 == 1) and (a or b)):
    res += 1

print(res)
