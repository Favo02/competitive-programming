import sys

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for line in lines:
  compressed = []

  last = ''
  count = 0
  for c in line:
    if c == last:
      count += 1
    else:
      compressed.append((count, last))
      last = c
      count = 1

  compressed.append((count, last))

  for c, l in compressed[1:]:
    for cc in str(c):
      res += int(cc)
    for ll in l:
      res += ord(ll) - ord('A') + 1

print(res)
