import sys

lines = []
for l in sys.stdin:
  lines.append(l[:-1])
lines = lines[1:]

multiset = {}

for l in lines:
  tkns = l.split(" ")
  op = tkns[0]
  l = int(tkns[1])
  r = int(tkns[2])
  if op == '+':
    if (l,r) in multiset:
      multiset[(l,r)] += 1
    else:
      multiset[(l,r)] = 1
  else:
    multiset[(l,r)] -= 1
    if multiset[(l,r)] == 0:
      del multiset[(l,r)]

  res = None
  if len(multiset) <= 1:
    res = False

  if res is None:
    segs = list(multiset.keys())
    segs.sort(key=lambda t: t[1])
    # print(segs)
    for i, s1 in enumerate(segs):
      if i == len(segs)-1:
        continue
      s2 = segs[-1]
      if s2[0] > s1[1]:
        res = True
        break
    else:
      res = False

  print("YES" if res else "NO")
