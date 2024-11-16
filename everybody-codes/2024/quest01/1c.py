res = 0

s = input()

cost = {
  "A": 0,
  "B": 1,
  "C": 3,
  "D": 5,
}

for i in range(0, len(s), 3):

  stack = 0

  for ii in range(i, i+3):
    if s[ii] in cost:
      stack += 1
      res += cost[s[ii]]

  if stack == 3:
    res += 6
  if stack == 2:
    res += 2

print(res)
