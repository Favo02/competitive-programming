import sys

res = 0
lines = sys.stdin.read().strip().splitlines()

for i, l in enumerate(lines):
  if l == "TRUE":
    res += i+1

print(res)
