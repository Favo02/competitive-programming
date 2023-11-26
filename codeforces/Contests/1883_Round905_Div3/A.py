# f = open("1.in", "r")
# lines = f.read().splitlines()[1:]


pad = [1,2,3,4,5,6,7,8,9,0]
# print(lines)

import sys

for li, l in enumerate(sys.stdin):
  if li == 0: continue
  # print(l)
  cursor = 0
  secs = 4
  secs += abs(0 - pad.index(int(l[0])))
  for i in range(3):
    dist = abs(pad.index(int(l[i])) - pad.index(int(l[i+1])))
    secs += dist
  print(secs)
