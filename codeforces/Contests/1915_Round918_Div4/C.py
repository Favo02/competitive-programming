from math import sqrt

cases = int(input())

for _ in range(cases):
  n = int(input())
  blocks = sum([int(nn) for nn in input().split()])
  if int(sqrt(blocks)) == sqrt(blocks):
    print("YES")
  else:
    print("NO")
