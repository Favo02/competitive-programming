nk = input().split(" ")
nbus, k = int(nk[0]), int(nk[1])
print(k)

costoGiorni = {}

for _ in range(nbus):
  tokens = [int(n) for n in input().split(" ")]

  s, e, c = tokens[0], tokens[1], tokens[2]
  print(s,e,c)
