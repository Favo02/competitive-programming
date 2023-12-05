from collections import defaultdict

cases = int(input())

while cases > 0:
  cases -= 1
  lenn = int(input())
  str = input()

  tot = 0
  maxx = 0
  occs = defaultdict(int)
  for c in str:
    occs[c] += 1
    maxx = max(maxx, occs[c])

  rems = max(0, lenn-maxx)

  res = max(0, maxx - rems)

  if (res == 0) and (len(str) % 2 == 1):
    print(res+1)
  else:
    print(res)
