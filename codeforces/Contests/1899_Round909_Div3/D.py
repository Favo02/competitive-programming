import sys
from math import log2

cases = int(input())

lines = []
for l in sys.stdin:
  lines.append(l.rstrip('\n'))

for i in range(0, len(lines), 2):
  count = 0
  nums = [int(w) for w in lines[i+1].split(" ")]
  # print(nums)

  for i in range(0, len(nums)):
    for j in range(i, len(nums)):
      if i == j: continue

      a = nums[i]
      b = nums[j]

      if a == b:
        count += 1
        continue

      n = (log2(a) + b)
      m = (log2(b) + a)

      if n == m:
        count += 1


  print(count)
