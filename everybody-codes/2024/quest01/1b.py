res = 0

s = input()

cost = {
  "A": 0,
  "B": 1,
  "C": 3,
  "D": 5,
}

for i in range(0, len(s), 2):

  if s[i] in cost and s[i+1] in cost:
    res += cost[s[i]] + cost[s[i+1]] + 2

  else:
    res += cost.get(s[i], 0) + cost.get(s[i+1], 0)

print(res)
