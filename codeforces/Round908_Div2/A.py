import sys

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for l in lines:
  if not l.isdigit():
    print(l[-1])
