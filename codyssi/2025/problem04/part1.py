import sys

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for line in lines:
  for c in line:
    res += ord(c) - ord('A') + 1
print(res)
