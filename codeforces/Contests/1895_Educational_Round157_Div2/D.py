import sys

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

nums = int(lines[0])
target = lines[1].split(" ")
target = [int(n) for n in target]

res = []

for start in range(nums):

  n = start
  for ti in target:
    res.append(n)
    next = ti ^ n
    if next >= nums or next in res:
      res = []
      break
    n = next
  else:
    res.append(n)
    break

for r in res:
  print(r, end=" ")
print()
