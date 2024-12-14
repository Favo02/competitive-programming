scores = list(map(int, input().split()))
names = "ABCDE"
res = []

for who in range(1 << 5):
  sc = 0
  name = []
  for i in range(5):
    if who & (1 << i) != 0:
      sc += scores[i]
      name.append(names[i])
  res.append((-sc, "".join(name)))

res.sort()

for s, name in res:
  if s != 0:
    print(name)
