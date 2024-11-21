steps = input().split(",")

res = 0
h = 0

for s in steps:

  if s[0] == "U":
    h += int(s[1:])

  if s[0] == "D":
    h -= int(s[1:])

  res = max(res, h)

print(res)
