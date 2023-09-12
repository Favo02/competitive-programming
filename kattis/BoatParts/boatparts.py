import sys

input = []
for line in sys.stdin:
  input.append(line)

t = input[0].split(" ")
parts = int(t[0])
seas = int(t[1])
inputs = input[1:]

day = 1
changed = set()
found = False
for p in inputs:
  if not p in changed:
    changed.add(p)
  if len(changed) == parts:
    print(day)
    found = True
    break
  day+=1

if not found:
  print("paradox avoided")
