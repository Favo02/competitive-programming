import sys

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

print(lines)
