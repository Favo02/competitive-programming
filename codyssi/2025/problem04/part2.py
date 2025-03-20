import sys

lines = list(map(str.strip, sys.stdin.readlines()))

res = 0
for line in lines:
  initchars = len(line) // 10
  newline = line[:initchars] + str(len(line)-2*initchars) + line[-initchars:]
  for c in newline:
    if c.isdigit():
      res += int(c)
    else:
      res += ord(c) - ord('A') + 1
print(res)
