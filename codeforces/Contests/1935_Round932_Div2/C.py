cases = int(input())

def solve(cur, time, used, res):
  oldres = res
  for i in range(LEN):
    if (used & (1 << i)) != 0: continue

    newT = time + abs(msgs[cur][1] - msgs[i][1]) + msgs[i][0]
    if newT == TIME:
      res = max(res, oldres+1)
    elif newT < TIME:
      used |= (1 << i)
      res = max(res, solve(i, newT, used, oldres+1))
  return res

for _ in range(cases):

  INF = float("inf")

  LEN, TIME = [int(n) for n in input().split()]
  # print(LEN, TIME)

  msgs = []
  for n in range(LEN):
    a,b = [int(n) for n in input().split()]
    if a > TIME: continue
    msgs.append((a,b))

  LEN = len(msgs)

  res = 0
  for i in range(LEN):
    if msgs[i][0] > TIME: continue
    res = max(res, solve(i, msgs[i][0], 1 << i, 1))
  print(res)
