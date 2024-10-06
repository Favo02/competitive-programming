nk = input().split(" ")
nbus, k = int(nk[0]), int(nk[1])

costoGiorni = {}

for _ in range(nbus):
  tokens = [int(n) for n in input().split(" ")]

  s, e, c = tokens[0], tokens[1], tokens[2]

  for n in range(s, e+1):
    if n in costoGiorni:
      costoGiorni[n] += c
    else:
      costoGiorni[n] = c

print(costoGiorni)

res = 0
for c,v in costoGiorni.items():
  if k < v:
    res += k
  else:
    res += v

print(res)
