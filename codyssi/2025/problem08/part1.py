import sys

lines = sys.stdin.read().strip().splitlines()
res = 0

for l in lines:
  for c in l:
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
      res += 1

print(res)
